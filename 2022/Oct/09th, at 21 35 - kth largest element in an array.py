class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        offset = 10000
        # bucket sort, bad space, linear time
        buckets = [[] for i in range(offset * 2 + 1)]
        
        for num in nums:
            buckets[num + offset].append(num)
        

        count = 0
        value = None
        for i in range(len(buckets) - 1, -1, -1):
            if len(buckets[i]) > 0:
                while count < k and len(buckets[i]) > 0:
                    value = buckets[i].pop()
                    count += 1
            if count == k:
                break
        return value
                    