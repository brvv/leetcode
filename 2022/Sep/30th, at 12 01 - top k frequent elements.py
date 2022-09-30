class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for item in nums:
            if item not in freq:
                freq[item] = 1
            else:
                freq[item] += 1
                
        return sorted(freq, key=freq.get, reverse=True)[:k]