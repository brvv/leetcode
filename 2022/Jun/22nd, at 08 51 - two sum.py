class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} 
        for index1, num in enumerate(nums):
            diff[target - num] = index1
        
        print(diff)
        
        for index2, num in enumerate(nums):
            if num in diff.keys() and index2 != diff[num]:
                print(num)
                return [diff[num], index2]
            