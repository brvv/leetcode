class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        #prove all global inversions are local inversions
        #prove there are no global inversions (that are not local inversions)

        if len(nums) < 3:
            return True

        smallest_right = [None for i in nums]
        smallest_right[-1] = nums[-1]
        smallest_right[-2] = min(smallest_right[-1], nums[-2])

        for i in range(len(nums) - 3, -1 , -1):
            smallest_right[i] = min(smallest_right[i + 1], nums[i])
            
            if nums[i] > smallest_right[i + 2]:
                return False
        return True
