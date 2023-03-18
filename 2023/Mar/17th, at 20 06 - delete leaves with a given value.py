# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        parents = {}

        def populateParents(node, prevNode):
            if node is None:
                return

            if prevNode is not None:
                parents[node] = prevNode

            populateParents(node.left, node)
            populateParents(node.right, node)

        populateParents(root, None)
        
        leaves = []

        def getLeaves(node):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                leaves.append(node)
            
            getLeaves(node.left)
            getLeaves(node.right)
        getLeaves(root)
        

        while True:
            newLeaves = []

            while len(leaves) > 0:
                leaf = leaves.pop()
                if leaf.val == target:
                    #if leaf not in parents, it doesnt have a parent, return empty
                    if leaf not in parents:
                        return None

                    leaf_parent = parents[leaf]

                    if leaf_parent.left == leaf:
                        leaf_parent.left = None
                    elif leaf_parent.right == leaf:
                        leaf_parent.right = None

                    #check if parent becomes leaf
                    if leaf_parent.left is None and leaf_parent.right is None:
                        newLeaves.append(leaf_parent)

            
            if len(newLeaves) > 0:
                leaves = newLeaves
            else:
                break
        return root


            











