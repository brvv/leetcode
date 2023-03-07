class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        array = nums + nums[0 : -1]
        max_sums = [0 for item in nums]
        min_sums = [0 for item in nums]
        max_sums[-1] = nums[-1]
        min_sums[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            max_sums[i] = max(nums[i], nums[i] + max_sums[i + 1])
            min_sums[i] = min(nums[i], nums[i] + min_sums[i + 1])
        print(max_sums)
        print(min_sums)
        print(sum(nums))

        max_sum = max(max_sums)
        min_sum = sum(nums) - min(min_sums)

        if min_sum == 0:
            return max_sum

        return max(max(max_sums), sum(nums) - min(min_sums))


