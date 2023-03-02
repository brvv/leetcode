# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return root
        rootVal = root.val
        root.val = 101
        traversal = []

        def dfs(node):
            if node is None:
                return
            if node.val != 101:
                traversal.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        ptr = 0

        node = root

        while node and ptr < len(traversal):
            node.right = traversal[ptr]
            node.left = None
            ptr += 1
            node = node.right
        root.val = rootVal
        
        print([node.val for node in traversal])