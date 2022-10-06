"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned_nodes = set({})
        
        if node is None:
            return None
        
        new_graph = {}
        startNodeVal = node.val
        new_graph[startNodeVal] = Node(node.val, [])
        #stack consisting of old nodes that have to be cloned
        stack = [node]
        
        
        while stack:
            old_node = stack.pop()
            
            if old_node.val in cloned_nodes:
                continue
                
            new_node = new_graph[old_node.val]
            old_node_neighbours = old_node.neighbors
            
            for old_neighbour in old_node_neighbours:

                if not old_neighbour.val in new_graph:
                    new_graph[old_neighbour.val] = Node(old_neighbour.val, [])
                    
                new_neighbour = new_graph[old_neighbour.val]
                new_node.neighbors.append(new_neighbour)
                
                stack.append(old_neighbour)
                
            cloned_nodes.add(new_node.val)

            
        return new_graph[startNodeVal]