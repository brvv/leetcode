class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        cache = set({})

        def dfs(currPoint):
            if currPoint[0] == 1 or currPoint[1] == 1:
                return True
            elif currPoint[0] <= 0 or currPoint[1] <= 0:
                return False

            subproblem = tuple(currPoint)
            if subproblem in cache:
                return False
            cache.add(subproblem)

            ans = False
            next_X = currPoint[0] - currPoint[1]
            next_Y = currPoint[1] - currPoint[0]

            if currPoint[0] % 2 == 0:
                ans = ans or dfs([currPoint[0] // 2, currPoint[1]])
            elif next_X % 2 == 0:
                ans = ans or dfs([next_X, currPoint[1]])
                
            if ans:
                return ans

            if currPoint[1] % 2 == 0:
                ans = ans or dfs([currPoint[0], currPoint[1] // 2])
            elif next_Y % 2 == 0:
                ans = ans or dfs([currPoint[0], next_Y])
            return ans
        
        return dfs([targetX, targetY])