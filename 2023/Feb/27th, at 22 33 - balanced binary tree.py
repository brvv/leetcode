# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedRec(node):
            if node is None:
                return 0
            
            left_height = isBalancedRec(node.left)
            right_height = isBalancedRec(node.right)

            
            height = 1 + max(left_height, right_height)

            if abs(left_height - right_height) > 1:
                return 1000000000
            else:
                return height 
        
        return isBalancedRec(root) < 1000000000