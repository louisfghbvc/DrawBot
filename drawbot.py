from pynput.mouse import Controller, Button
from PIL import Image
import time
from urllib.request import urlopen, Request
from collections import defaultdict
import numpy as np

mouse = Controller()

class DrawBot:
    def __init__(self, desiredWidth, desiredHeight, startPosition, ignoreSoloPixels, dither, speed, pixelInterval, url, colors, coordinates, isDfs, isEdge):
        self.colorCoordinates = coordinates
        self.colors = colors
        self.ignoreSoloPixels = ignoreSoloPixels
        self.pixelInterval = pixelInterval
        self.isDfs = isDfs
        self.isEdge = isEdge
        self.speed = self.convertSpeed(speed)
        self.speedByPixel = self.convertSpeedByPixel(speed)
        self.startPosition = startPosition
        self.setUpColorPalettes(colors)
        self.setUpImageToDraw(url, dither, desiredWidth, desiredHeight)
        self.pixelLinesToDraw = self.extractPixelLinesToDraw(pixelInterval, ignoreSoloPixels)
        self.vis = np.zeros((self.height, self.width))
    
    def setUpImageToDraw(self, url, dither, desiredWidth, desiredHeight):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = Request(url=url, headers=headers)
        self.img = Image.open(urlopen(req))
        fillColor = (255,255,255)
        self.img = self.img.convert("RGBA")
        if self.img.mode in ('RGBA', 'LA'):
            background = Image.new(self.img.mode[:-1], self.img.size, fillColor)
            background.paste(self.img, self.img.split()[-1])
            self.img = background
        self.img = self.img.convert("RGB").quantize(palette=self.palette, dither=dither)
        self.width, self.height = self.convertSize(desiredWidth, desiredHeight)
        self.img = self.img.convert("RGB")

    def setUpColorPalettes(self, colors):
        paletteColors = colors
        for i in range(768-len(colors)):
            paletteColors.append(0)
        self.palette = Image.new("P", (16, 16))
        self.palette.putpalette(paletteColors)
    
    def changeColor(self, r, g, b):
        found = False
        for i in range(0, len(self.colors), 3):
            if r == self.colors[i] and g == self.colors[i+1] and b == self.colors[i+2]:
                mouse.position = self.colorCoordinates[int(i/3)]
                found = True
                break
        if found:
            self.click()

    def extractPixelLinesToDraw(self, pixelInterval, ignoreSoloPixels):
        drawVerticallyLines, nbLinesVertical = self.extractLinesToDraw(True, pixelInterval, ignoreSoloPixels)
        drawHorizontallyLines, nbLinesHorizontal = self.extractLinesToDraw(False, pixelInterval, ignoreSoloPixels)
        if nbLinesHorizontal <= nbLinesVertical:
            return drawHorizontallyLines
        return drawVerticallyLines

    def getEdges(self, points, remainOrder = True):
        '''get img edge by each components, remain origin order'''
        ans = set()
        # first by h, second by w
        for turn in range(2):
            bound = self.width if turn else self.height
            each_mx = defaultdict(int)
            each_mn = defaultdict(lambda:1e5)
            for p in points:
                h, w = p[0^turn], p[1^turn]
                each_mx[h] = max(each_mx[h], w)
                each_mn[h] = min(each_mn[h], w)
            for v in range(bound):
                if v in each_mx:
                    mx_point = (each_mx[v], v) if turn else (v, each_mx[v])
                    mn_point = (each_mn[v], v) if turn else (v, each_mn[v])
                    ans.add(mx_point)
                    ans.add(mn_point)
        return list(filter(lambda e: e in ans, points)) if remainOrder else list(ans)

    def test_levelPixels(self, i, j, color, exit_event, level):
        '''test img have enough pixels to draw'''
        todo = [(i, j)]
        while todo and level >= 0:
            if exit_event.is_set(): return
            i, j = todo.pop()
            nxt = [(i+self.pixelInterval,j), (i-self.pixelInterval,j), (i,j+self.pixelInterval), (i,j-self.pixelInterval)]
            for ni, nj in nxt:
                if not (0 <= ni < self.height) or not (0 <= nj < self.width) or self.vis[ni][nj] or color != self.img.getpixel((nj, ni)): continue
                if level == 0: return True
                todo.append((ni, nj))
            level -= 1
        return False

    def drawPerPixel(self, i, j):
        mouse.position = (j + self.startPosition[0], i + self.startPosition[1])
        time.sleep(self.speedByPixel)
        self.click()
        time.sleep(self.speedByPixel)
    
    def drawPixels(self, points, exit_event):
        for i, j in points:
            if exit_event.is_set(): return
            self.drawPerPixel(i, j)

    def dfs(self, i, j, color, exit_event, drawing = True):
        '''traversal with same color'''
        callback = []
        todo = [(i, j)]
        while todo:
            if exit_event.is_set(): return
            i, j = todo.pop()
            if not (0 <= i < self.height) or not (0 <= j < self.width) or self.vis[i][j] or color != self.img.getpixel((j, i)): continue
            self.vis[i][j] = 1
            callback.append((i, j))
            if drawing: self.drawPerPixel(i, j)
            todo += [(i+self.pixelInterval,j), (i-self.pixelInterval,j), (i,j+self.pixelInterval), (i,j-self.pixelInterval)]
        return callback

    def dfsDraw(self, exit_event):
        for i in range(0, self.height, self.pixelInterval):
            for j in range(0, self.width, self.pixelInterval):
                if exit_event.is_set(): return
                color = self.img.getpixel((j, i))
                if self.vis[i][j] or color == (255,255,255) or color == (0,0,0) : continue
                if self.ignoreSoloPixels and not self.test_levelPixels(i, j, color, exit_event, self.pixelInterval): continue
                self.changeColor(color[0], color[1], color[2])
                if self.isEdge:
                    points = self.dfs(i, j, color, exit_event, drawing=False)
                    points = self.getEdges(points)
                    self.drawPixels(points, exit_event)
                else:
                    self.dfs(i, j, color, exit_event, drawing=True)
                time.sleep(self.speedByPixel)
        # black
        for i in range(0, self.height, self.pixelInterval):
            for j in range(0, self.width, self.pixelInterval):
                if exit_event.is_set(): return
                color = self.img.getpixel((j, i))
                if self.vis[i][j] or color != (0,0,0) : continue
                if self.ignoreSoloPixels and not self.test_levelPixels(i, j, color, exit_event, self.pixelInterval): continue
                self.changeColor(color[0], color[1], color[2])
                if self.isEdge:
                    points = self.dfs(i, j, color, exit_event, drawing=False)
                    points = self.getEdges(points)
                    self.drawPixels(points, exit_event)
                else:
                    self.dfs(i, j, color, exit_event, drawing=True)
                time.sleep(self.speedByPixel)

    def extractLinesToDraw(self, vertically, pixelInterval, ignoreSoloPixels):
        '''Get the lines to draw vertically or horizontally'''
        if not vertically:
            bound1 = self.height
            bound2 = self.width
        else:
            bound1 = self.width
            bound2 = self.height
        lines = defaultdict(list)
        nbLinesToDraw = 0
        for i in range(0, bound1, pixelInterval):
            lineColor = None
            for j in range(0, bound2, pixelInterval):
                if not vertically:
                    r, g, b = self.img.getpixel((j, i))
                else:
                    r, g, b = self.img.getpixel((i, j))
                if not vertically:
                    currentPosition = (j+self.startPosition[0], i+self.startPosition[1])
                else:
                    currentPosition = (i+self.startPosition[0], j+self.startPosition[1])
                if lineColor == None:
                    lineColor = (r, g, b)
                    lineStart = currentPosition
                elif lineColor != (r, g, b):
                    if (ignoreSoloPixels and lineStart != lineEnd) or not ignoreSoloPixels:
                        lines[lineColor].append([lineStart, lineEnd])
                    if lineColor != (255,255,255):
                        nbLinesToDraw += 1
                    lineColor = (r, g, b)
                    lineStart = currentPosition
                lineEnd = currentPosition
            if (ignoreSoloPixels and lineStart != lineEnd) or not ignoreSoloPixels:
                lines[lineColor].append([lineStart, lineEnd])
            if lineColor != (255,255,255):
                nbLinesToDraw += 1
            lineColor = None
        return [lines, nbLinesToDraw]
    
    def draw(self, exit_event):
        if self.isDfs:
            self.dfsDraw(exit_event)
            return

        for key, value in self.pixelLinesToDraw.items():
            if key != (255,255,255) and key != (0,0,0):
                self.changeColor(key[0], key[1], key[2])
                for j in value:
                    if exit_event.is_set(): break
                    self.drawLine(j)
                
            if self.speed == 0.1 or self.speed == 0.00001:
                time.sleep(0.1)
        # black
        if (0,0,0) in self.pixelLinesToDraw:
            self.changeColor(0, 0, 0)
            for j in self.pixelLinesToDraw[(0,0,0)]:
                if exit_event.is_set(): break
                self.drawLine(j)
    
    def drawLine(self, coordinates):
        mouse.position = coordinates[0]
        mouse.press(Button.left)
        mouse.move(abs(coordinates[1][0] - coordinates[0][0]), abs(coordinates[1][1] - coordinates[0][1]))
        if (abs(coordinates[1][0] - coordinates[0][0]) > 0 or abs(coordinates[1][1] - coordinates[0][1]) > 0):
            time.sleep(self.speed)
        else:
            time.sleep(self.speedByPixel)
        mouse.release(Button.left)

    def convertSpeed(self, speed):
        if speed == 1:
            return 0.1
        if speed == 2:
            return 0.00001
        if speed == 3:
            return 0.000000001
        if speed == 4:
            return 0.0000000000000001
        
    def convertSpeedByPixel(self, speed):
        if speed == 1:
            return 0.00001
        if speed == 2:
            return 0.000000001
        if speed == 3:
            return 0.0000000000000001
        if speed == 4:
            return 0.0000000000000001
    
    def click(self):
        mouse.press(Button.left)
        mouse.release(Button.left)

    def convertSize(self, desiredWidth, desiredHeight):
        '''convert img to desiredWidth / desiredHeight keep aspect ratio'''
        maxSize = (desiredWidth, desiredHeight)
        if self.img.size[0] >= desiredWidth and self.img.size[1] >= desiredHeight:
            self.img.thumbnail(maxSize, Image.ANTIALIAS)
            return self.img.size
        h_ratio = desiredHeight / self.img.size[1]
        w_ratio = desiredWidth / self.img.size[0]
        if int(self.img.size[0] * h_ratio) < desiredWidth:
            maxSize = (int(self.img.size[0] * h_ratio), desiredHeight)
            self.img = self.img.resize(maxSize, Image.ANTIALIAS)
            return maxSize
        elif int(self.img.size[1] * w_ratio) < desiredHeight:
            maxSize = (desiredWidth, int(self.img.size[1] * w_ratio))
            self.img = self.img.resize(maxSize, Image.ANTIALIAS)
            return maxSize
        self.img.thumbnail(maxSize, Image.ANTIALIAS)
        return self.img.size