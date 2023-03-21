class Solution:
    def getParent(self, num):
        if num % 2 == 1:
            return (num - 1) // 2
        return num // 2

    def query(self, num1, num2):
        dist1 = 0
        dist2 = 0

        while num1 != num2:
            if num1 > num2:
                dist1 += 1
                num1 = self.getParent(num1)
            elif num2 > num1:
                dist2 += 1
                num2 = self.getParent(num2)
        return [num1, dist1, dist2]


    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []

        for num1, num2 in queries:
            res = self.query(num1, num2)
            cycleLen = 1 + res[1] + res[2]
            ans.append(cycleLen)
        return ans