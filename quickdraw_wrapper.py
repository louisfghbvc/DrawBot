import os
from quickdraw import QuickDrawData

class quickDrawWrapper:
    def __init__(self) -> None:
        self.qd = QuickDrawData()
        self.mName = self.matchName()

    def matchName(self):
        '''match translate name to english name'''
        name = os.path.dirname(os.path.abspath(__file__)) + "\\colorPalettes\\names.txt"
        res = dict()
        for i, v in enumerate(open(name, encoding='utf8').read().split()):
            res[v] = self.qd.drawing_names[i]
        return res

    def getDrawPosition(self, name):
        if name in self.mName:
            return self.qd.get_drawing(self.mName[name]).strokes
        return None

if __name__ == '__main__':
    # local test
    qd = quickDrawWrapper()
    for val in list(qd.mName.keys()):
        qd.getDrawPosition(val)