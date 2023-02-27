class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = len(nums) / 2
        integers = {}
        for integer in nums:
            if integer not in integers:
                integers[integer] = 1
            else:
                integers[integer] += 1
        
        for integer in integers:
            if integers[integer] == count:
                return integer
