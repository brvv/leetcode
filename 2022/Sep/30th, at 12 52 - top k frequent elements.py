class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [None for i in range(len(nums)+1)]
        # the trick is that the frequencies are unique
        for item in nums:
            count[item] = 1 + count.get(item, 0)
            
        for num, freq in count.items():
            if buckets[freq] is not None:
                buckets[freq].append(num)
            else:
                buckets[freq] = [num]
            
        #Use bucket sort
        #since frequencies are unique (and we only need top smth of them) order elements in terms of their frequency with bucket sort
        #then simply pop the required number of items
        
        res = []
        
        while len(res) < k:
            bucket = buckets.pop()
            
            if bucket is not None:
                for item in bucket:
                    res.append(item)
        return res
        