class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        doubles = maxDoubles
        while doubles > 0:
            if target == 1:
                return steps

            if target % 2 == 1:
                target -= 1
            else:
                target //= 2
                doubles -= 1
            steps += 1
        steps += target
        return steps - 1
             