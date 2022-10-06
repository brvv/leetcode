# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = []
        
        def dfs(root):
            if root.left == None and root.right == None:
                lst.append(root.val)
                return;
            
            if root.left != None:
                dfs(root.left)
            
            lst.append(root.val)
            
            if root.right != None:
                dfs(root.right)
                
            
        
        dfs(root)
        print(lst)
        for i in range(0, len(lst) - 1):
            item1 = lst[i]
            item2 = lst[i+1]
            
            if item2 <= item1:
                return False
        return True

            