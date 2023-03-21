class Solution:
    def getSmallestMonoNum(self, start):
        for i in range(len(start) - 1):
            first = int(start[i])
            second = int(start[i + 1])

            if first <= second:
                continue

            return start[0:i + 1] + (start[i] * (len(start) - i-1))

        return start

    def monotoneIncreasingDigits(self, n: int) -> int:
        low = 0
        high = n
        midNum = 0
        lastValid = 0

        while low <= high:
            mid = (high + low) // 2

            midNum = int(self.getSmallestMonoNum(str(mid)))
            print(low, high, mid, midNum)

            if midNum == high:
                return midNum

            if midNum < high:
                low = midNum + 1
                lastValid = midNum
            elif midNum > high:
                high = mid - 1
            else:
                return midNum
        
        return lastValid
            