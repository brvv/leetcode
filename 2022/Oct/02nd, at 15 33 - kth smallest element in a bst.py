# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        
        def dfs(root, k):
            print(root.val)
            if len(values) == k:
                return
            
            if root.left:
                dfs(root.left, k)
                
            values.append(root.val)
            
            if root.right:
                dfs(root.right, k)
        
        dfs(root,k)
        return values[k-1]
            