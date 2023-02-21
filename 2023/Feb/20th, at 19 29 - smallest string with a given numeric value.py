class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        max_offset = ord('z') - ord('a')
        budget = k - n
        res = [1 for i in range(n)]

        for i in range(len(res)):
            res[i] += min(budget, max_offset)
            budget -= min(budget, max_offset)
        print(res)
        ans = [chr(ord('a') + i - 1) for i in reversed(res)]
        return ''.join(ans)
        