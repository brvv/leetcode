class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set({})
        for i, val in enumerate(nums):
            if nums[abs(val) - 1] < 0:
                res.add(abs(val))
            nums[abs(val) - 1] = - abs(nums[abs(val) - 1])
        return res