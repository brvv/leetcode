# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = [[]]
        
        stack = []
        stack.append(root)
        
        level = 0
        
        while stack:
            newstack = []
            
            for node in stack:
                if node.left is not None:
                    newstack.append(node.left)
                if node.right is not None:
                    newstack.append(node.right)
                
                if level >= len(res):
                    res.append([])
                res[level].append(node.val)
            
            stack = newstack
            level += 1
            
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        return res
            
        
        
        