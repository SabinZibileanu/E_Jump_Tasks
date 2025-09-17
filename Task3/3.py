from math import sqrt

class IntelRadar:
    def possiblePoints(self, x1: int, y1: int, r1:int, x2: int, y2: int, r2:int) -> int:
        centersDist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if centersDist == 0:
            if r1 == r2:
                return -1
            else:
                return 0
            
        if (centersDist > r1 + r2) or (centersDist < abs(r1 - r2)):
            return 0

        elif (centersDist == r1 + r2) or (centersDist == abs(r1 - r2)):
            return 1
        
        return 2

ir = IntelRadar()
testCasesFiles = ['tc0.txt', 'tc1.txt', 'tc2.txt', 'tc3.txt']
testCaseResults = {
    0:2,
    1:1,
    2:0,
    3:-1
}
def run_tests():
    for idx, filePath in enumerate(testCasesFiles):
        with open(filePath, 'r') as testCaseFile:
            x1, y1, r1, x2, y2, r2 = [int(val) for val in testCaseFile.readlines()]
            result = ir.possiblePoints(x1, y1, r1, x2, y2, r2)
            assert result == testCaseResults[idx], f'Wrong result on test case {idx}'







