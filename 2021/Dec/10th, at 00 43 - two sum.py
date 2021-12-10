class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index in range(len(nums)):
            second = target - nums[index]
            if second in dict:
                return [dict[second], index]
            else:
                dict[nums[index]] = index