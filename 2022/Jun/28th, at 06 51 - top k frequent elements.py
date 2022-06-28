class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        order = [[] for i in range(len(nums))]
        for item in nums:
            dic[item] = 1 + dic.get(item, 0)
        for item, freq in dic.items():
            order[freq-1].append(item)
        
        vals = 0
        ans=[]
        print(order)
        for index in range(len(order)-1, -1, -1):
            for item in order[index]:
                ans.append(item)
                vals += 1
            if vals >= k:
                break
        return ans
                