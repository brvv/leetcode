class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum = sum(nums)
        self.rightSums = [0 for _ in nums]
        self.leftSums = [0 for _ in nums]
        
        self.rightSums[-1] = nums[-1]
        self.leftSums[0] = nums[0]
        
        for i in range(1, len(nums)):
            self.leftSums[i] = self.leftSums[i-1] + nums[i]

        for i in range(len(nums)-2, -1, -1):
            self.rightSums[i] = self.rightSums[i+1] + nums[i]

        
        

    def sumRange(self, left, right):
        leftsum = self.leftSums[left-1] if left > 0 else 0
        rightsum = self.rightSums[right + 1] if right < len(self.nums)-1 else 0
        
        return self.sum - (leftsum + rightsum)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)