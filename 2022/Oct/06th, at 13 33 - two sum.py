class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res=[]
        
        for i, num in enumerate(nums):
            res.append(target - num)
            dic[num] = i
            
        for i, smth in enumerate(res):
            if smth in dic and i != dic[smth]:
                return [i, dic[smth]]
