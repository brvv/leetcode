# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        tree = defaultdict(list)
        checked_nodes = {}

        def getTree(node):
            if node is None:
                return

            if node.left:
                tree[node.val].append(node.left.val)
                tree[node.left.val].append(node.val)

            if node.right:
                tree[node.val].append(node.right.val)
                tree[node.right.val].append(node.val)

            getTree(node.left)
            getTree(node.right)


        getTree(root)
        
        infected_nodes = [start]
        checked_nodes[start] = True
        minutes = -1

        while True:
            new_infected = []
            minutes += 1
            # get all adjacent infected nodes
            while infected_nodes:
                node = infected_nodes.pop()
                checked_nodes[node] = True
                adjacent_nodes = tree[node]

                for adj in adjacent_nodes:
                    if adj not in checked_nodes:
                        new_infected.append(adj)

            infected_nodes = new_infected
            if len(infected_nodes) == 0:
                break
        return minutes




















