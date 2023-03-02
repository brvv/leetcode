class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #lowest on left
        queue = deque([])

        count = 0
        while count < len(nums):
            item = nums[count]

            if item != 0 and len(queue) > 0:
                lowest = queue.popleft()
                nums[lowest], nums[count] = nums[count], nums[lowest]
                continue

            if item == 0:
                queue.append(count)
            
            count += 1
        
        return nums


