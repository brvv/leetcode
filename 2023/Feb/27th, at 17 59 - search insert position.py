class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] < target:
                    continue
                elif nums[i] > target:
                    return i
        return len(nums)