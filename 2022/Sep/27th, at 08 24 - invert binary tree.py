# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_node = root
        
        if curr_node is not None:
            curr_node.left, curr_node.right = curr_node.right, curr_node.left
            self.invertTree(curr_node.left)
            self.invertTree(curr_node.right)
            
            return curr_node