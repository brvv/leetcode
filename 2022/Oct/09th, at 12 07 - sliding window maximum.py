class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        first_window = nums[0:k]
        res = []
        
        #init first window
        for item in first_window:
            while len(queue) > 0 and queue[-1] < item:
                queue.pop()
            queue.append(item)
        res.append(queue[0])
        
        for i in range(1, len(nums) - k + 1):
            removed_item = nums[i - 1]
            added_item = nums[i + k - 1]
            
            if removed_item == queue[0]:
                queue.popleft()
            
            while len(queue) > 0 and queue[-1] < added_item:
                queue.pop()
            queue.append(added_item)
            
            res.append(queue[0])
            

        return res