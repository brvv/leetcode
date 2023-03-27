class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = []
        counts = defaultdict(int)

        for val in arr:
            counts[val] += 1
        
        for key in counts:
            heappush(heap, [counts[key], key])
        
        while k > 0:
            topval, topkey = heappop(heap)
            if topval <= k:
                k -= topval
            else:
                k = 0
                heappush(heap, [topval - k, topkey])
        return len(heap)

