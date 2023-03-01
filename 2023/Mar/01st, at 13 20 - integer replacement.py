class Solution:
    def integerReplacement(self, n: int) -> int:
        def dp(curr, steps):
            if curr == 1:
                return steps
            
            if curr % 2 == 0:
                return dp(curr / 2, steps + 1)
            else:
                inc = dp(curr + 1, steps + 1)
                dec = dp(curr - 1, steps + 1)
                return min(inc, dec)
        return dp(n, 0)