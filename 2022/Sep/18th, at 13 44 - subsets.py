class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dfs_stack = []
        powerset = []
        
        dfs_stack.append([])
        
        depth = 0
        
        while depth < len(nums):    
            new_stack = []
            
            while dfs_stack:
                current_item = dfs_stack.pop()
            
                new_stack.append((current_item.copy()) + [nums[depth]])
                new_stack.append(current_item.copy())
            
            dfs_stack = new_stack.copy()
            depth += 1
        
        return dfs_stack