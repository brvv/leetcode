# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def deepestSum(root, level=0):
            if root is None:
                return None
            
            if root.left is None and root.right is None:
                return (root.val, level)
            
            left = deepestSum(root.left, level + 1)
            right = deepestSum(root.right, level + 1)
            
            if left is None:
                return right
            
            if right is None:
                return left
            
            if left[1] > right[1]:
                return left
            
            if right[1] > left[1]:
                return right
            
            return (left[0] + right[0], left[1])
            
            
            
            
        res = deepestSum(root)
        return res[0]