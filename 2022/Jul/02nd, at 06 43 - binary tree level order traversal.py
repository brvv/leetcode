# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        depth = 0
        levels = []
        current_nodes = []
        current_nodes.append(root)
        next_nodes = []
        
        
        
        while current_nodes:
            level = []
            
            for node in current_nodes:
                if not node:
                    continue
                
                level.append(node.val)
                
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
                    
            current_nodes = next_nodes.copy()
            next_nodes = []
            levels.append(level)
        return levels
                
            