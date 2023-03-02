# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth=0):
            if node is None:
                return [-1, 0]

            left = dfs(node.left, depth + 1)
            [left_depth, left_passing] = [left[0] + 1, left[1]]

            right = dfs(node.right, depth + 1)
            [right_depth, right_passing] = [right[0] + 1, right[1]]

            ans = [max(left_depth, right_depth), max(left_passing, right_passing, left_depth + right_depth)]
            return ans
        
        ans = dfs(root)
        return max(ans)
        