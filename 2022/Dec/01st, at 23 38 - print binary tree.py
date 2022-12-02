# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def findTreeHeight(root, level=1):
            if root == None:
                return level - 1
            
            left = findTreeHeight(root.left, level + 1)
            right = findTreeHeight(root.right, level + 1)
            
            
            return max(left, right)
        
        def placeVals(node, col, row, height):
            if row >= height:
                return
            if node == None:
                return
            table[row][col] = str(node.val)
            
            placeVals(node.left, col - 2 ** (height - row - 2) , row + 1, height)
            placeVals(node.right, col + 2 ** (height - row - 2) , row + 1, height)
            
        
        height = findTreeHeight(root)
        n = (2 ** (height))-1
        m = height
        
        table = [['' for i in range(n)] for j in range(m)]
        

        init_row = 0
        init_col = (n-1)//2
        
        placeVals(root, init_col, init_row, height)
        return table