# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        start_root = root
        
        def invert(node):
        
            if node is None:
                return

            node.right, node.left = node.left, node.right

            self.invertTree(node.left)
            self.invertTree(node.right)
        invert(root)
        return start_root