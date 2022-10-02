# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getParentPath(root, targetVal, path=[]):
            if (root == None):
                return None
            
            if root.val == targetVal:
                
                return path + [root]
            
            left = getParentPath(root.left, targetVal, path+[root])
            right = getParentPath(root.right, targetVal, path+[root])
            
            if left is not None:
                return left
            else:
                return right
        
        p_path = getParentPath(root, p.val)
        q_path = getParentPath(root, q.val)
        
        lastRoot = None
        
        for item1, item2 in zip(p_path, q_path):
            if item1.val == item2.val:
                lastRoot = item1
                continue
            else:
                break
        return lastRoot
            