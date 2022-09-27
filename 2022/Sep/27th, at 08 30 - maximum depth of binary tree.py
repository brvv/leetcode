# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def goDeeper(root, curr_depth = 0):
            if root is None:
                return curr_depth
            
            left_depth = goDeeper(root.left, curr_depth + 1)
            right_depth = goDeeper(root.right, curr_depth + 1)            
            return max(left_depth, right_depth)
        
        return goDeeper(root, 0)