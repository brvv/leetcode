# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif q.val == p.val:
            left_identical = self.isSameTree(p.left, q.left)
            right_identical = self.isSameTree(p.right, q.right)
            
            return left_identical and right_identical
        else:
            return False