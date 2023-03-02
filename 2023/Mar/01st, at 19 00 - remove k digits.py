class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        targetNum = str(num)
        targetLength = len(targetNum) - k

        cache = {}

        if targetLength == 0:
            return '0'

        #dp solution, TLE
        def dp(currNum, currIndex, targetNum : str, targetLength : int):
            if len(currNum) == targetLength:
                return int(currNum)
            elif currIndex >= len(targetNum):
                return 100000000000000000
            elif tuple([currNum, currIndex]) in cache:
                return cache[tuple([currNum, currIndex])]

            pick = dp(currNum + targetNum[currIndex], currIndex + 1, targetNum, targetLength)
            skip = dp(currNum, currIndex + 1, targetNum, targetLength)
            cache[tuple([currNum, currIndex])] = min(pick, skip)
            return cache[tuple([currNum, currIndex])]
        
        #stack solution
        def rKstack(targetNum, max_pops):
            stack = []
            pops = max_pops

            for i in targetNum:
                digit = int(i)

                while len(stack) > 0 and pops > 0 and stack[-1] > digit:
                    stack.pop()
                    pops-=1
                stack.append(digit)
                
            while pops > 0:
                stack.pop()
                pops-=1
                
            return str(int(''.join([str(i) for i in stack])))
        return rKstack(targetNum, k)

    #stack solution
    