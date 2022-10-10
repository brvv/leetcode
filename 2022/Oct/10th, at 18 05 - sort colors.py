class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {}
        for val in nums:
            dic[val] = 1 + dic.get(val, 0)
            
        for i in range(len(nums)):
            val = None
            if 0 in dic and dic[0] >= 1:
                val = 0
                dic[0] -=1
            elif 1 in dic and dic[1] >= 1:
                val = 1
                dic[1]-=1
            elif 2 in dic:
                val = 2
                dic[2]-=1
            nums[i] = val
        return nums
            