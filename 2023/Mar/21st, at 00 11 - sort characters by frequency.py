class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        counts = defaultdict(int)
        for letter in s:
            counts[letter] += 1
        
        for key in counts:
            heappush(heap, [-counts[key], key])

        res = []

        while len(heap) > 0:
            item = heappop(heap)
            res += [item[1]] * -item[0]
        return ''.join(res)
