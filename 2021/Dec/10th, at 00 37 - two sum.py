class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indexnum1 in range(len(nums)):
            for indexnum2 in  range(len(nums[indexnum1:])):
                if nums[indexnum1] + nums[indexnum2+indexnum1] == target:
                    if indexnum1 != indexnum2+indexnum1:
                        return [indexnum1, indexnum2+indexnum1]