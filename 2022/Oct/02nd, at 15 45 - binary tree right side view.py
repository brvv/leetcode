# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        rightside = []
        
        if root is None:
            return []
        
        stack.append(root)
        
        while True:
            if stack == []:
                break
            
            rightmost = stack[-1]
            rightside.append(rightmost.val)
            
            newstack = []
            
            for item in stack:
                if item.left:
                    newstack.append(item.left)
                if item.right:
                    newstack.append(item.right)
                    
            stack = newstack
            
        return rightside
            