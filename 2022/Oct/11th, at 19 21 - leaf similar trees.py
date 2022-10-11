# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []
        
        def dfs(root, seq):
            if root.left is None and root.right is None:
                seq.append(root.val)
                return
            
            if root.left:
                dfs(root.left, seq)
                
            if root.right:
                dfs(root.right, seq)
                
        dfs(root1, seq1)
        dfs(root2, seq2)
        
        
        if len(seq1) != len(seq2):
            return False
        
        for l1, l2 in zip(seq1, seq2):
            if l1 != l2:
                return False
        return True
                
        