class Solution:
    def tribonacci(self, n: int) -> int:
        cache = []
        cache.append(0)
        cache.append(1)
        cache.append(1)

        for i in range(3, n + 1):
            cache.append(cache[i - 1] + cache[i - 2] + cache[i - 3])
        return cache[n]