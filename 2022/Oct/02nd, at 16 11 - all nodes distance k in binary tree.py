# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        nodes = defaultdict(list)
        
        def graphify(root, parentVal=None):
            if root is not None:
                if parentVal is not None:
                    nodes[root.val].append(parentVal)
                
                if (root.left):
                    nodes[root.val].append(root.left.val)
                    graphify(root.left, parentVal = root.val)
                if (root.right):
                    nodes[root.val].append(root.right.val)
                    graphify(root.right, parentVal = root.val)
                
        graphify(root)
        
        rootVal = target.val
        res = []
        visited = {}
        visited[rootVal] = True
        stack = []
        stack.append(rootVal)
        distance = 0
        
        while True:
            newStack = []
            
            if distance == k:
                break
            
            while stack:
                elem = stack.pop()
                visited[elem] = True
                neighbours = nodes[elem]
                    
                for node in neighbours:
                    if node not in visited:
                        newStack.append(node)
            
            stack = newStack
            distance += 1
            
        return stack  
        
        