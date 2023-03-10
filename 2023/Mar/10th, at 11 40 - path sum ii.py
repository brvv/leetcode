# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, currSum, targetSum):
            if node is None:
                return

            newpath = path + [node.val]
            newsum = currSum + node.val

            if targetSum == newsum and node.left is None and node.right is None:
                res.append(newpath.copy())

            dfs(node.right, newpath, newsum, targetSum)
            dfs(node.left, newpath, newsum, targetSum)

        dfs(root, [], 0, targetSum)
        return res
