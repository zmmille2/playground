from collections import defaultdict

class Test:
    def __init__(self, num_points = 0):
        self.xeye = []
        self.xeyo = []
        self.xoye = []
        self.xoyo = []
        self.num_points = num_points
        self.winners = 0

    def addPoint(self, pair):
        x = pair[0]
        y = pair[1]
        if x % 2 == 0:
            if y % 2 == 0:
                self.xeye.append((x,y))
            else:
                self.xeyo.append((x,y))
        else:
            if y % 2 == 0:
                self.xoye.append((x,y))
            else:
                self.xoyo.append((x,y))

    def calculateWinners(self):
        x1 = len(self.xeye)
        x2 = len(self.xeyo)
        x3 = len(self.xoye)
        x4 = len(self.xoyo)
        self.winners += (x1 * (x1 - 1)) / 2
        self.winners += (x2 * (x2 - 1)) / 2
        self.winners += (x3 * (x3 - 1)) / 2
        self.winners += (x4 * (x4 - 1)) / 2
        print self.winners
        

if __name__ == "__main__":

    num_tests = int(raw_input())
    
    while num_tests > 0:
        num_tuples = int(raw_input())
        currentTest = Test(num_tuples)
        while num_tuples > 0:
            currentTest.addPoint(tuple(map(int, raw_input().split(' '))))
            num_tuples -= 1
        currentTest.calculateWinners()
        num_tests -= 1
