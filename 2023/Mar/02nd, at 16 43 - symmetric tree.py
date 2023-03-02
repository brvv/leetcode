# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            elif not leftNode or not rightNode:
                return False
            
            if leftNode.val != rightNode.val:
                return False
            
            left = dfs(leftNode.left, rightNode.right)
            right = dfs(leftNode.right,  rightNode.left)
            return left and right
        
        return dfs(root.left, root.right)
        