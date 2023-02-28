# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
                return TreeNode(val)

        def insert(currNode, val):

            
            if currNode.val > val:
                if currNode.left is not None:
                    insert(currNode.left,val)
                else:
                    currNode.left = TreeNode(val)
                    return
            
            elif currNode.val < val:
                if currNode.right is not None:
                    insert(currNode.right, val)
                else:
                    currNode.right = TreeNode(val)
                    return
        
        insert(root, val)
        return root