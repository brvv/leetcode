class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        existing_nums = set({})
        smallest_missing = 1
        
        for num in nums:
            if num == smallest_missing:
                smallest_missing += 1
                while smallest_missing in existing_nums:
                    smallest_missing += 1
            existing_nums.add(num)
        return smallest_missing