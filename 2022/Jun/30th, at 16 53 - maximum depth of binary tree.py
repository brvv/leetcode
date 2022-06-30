# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthHelper(self, root: TreeNode, depth = 1) -> int:
        if not root:
            return 0
        else:
            if root.left and root.right:
                return max(self.maxDepthHelper(root.left, depth + 1), self.maxDepthHelper(root.right, depth + 1))
            elif root.left:
                return self.maxDepthHelper(root.left, depth + 1)
            elif root.right:
                return self.maxDepthHelper(root.right, depth + 1)
            else:
                return depth
        
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root)