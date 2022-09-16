class Solution:
    def findSet(self, graphs, edge):
        for graph_i, graph in enumerate(graphs):
            if edge in graph:
                return graph_i
        return -1
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphs = []
        connected_nodes = set()
        
        for edge in edges:
            if (edge[0] not in connected_nodes and edge[1] not in connected_nodes):
                connected_nodes.add(edge[0])
                connected_nodes.add(edge[1])
                graphs.append(set({edge[0], edge[1]}))
                continue
            
            elif (edge[0] not in connected_nodes):
                connected_nodes.add(edge[0])
                setNum = self.findSet(graphs, edge[1])
                graphs[setNum].add(edge[0])
                continue
                
            elif (edge[1] not in connected_nodes):
                connected_nodes.add(edge[1])
                setNum = self.findSet(graphs, edge[0])
                graphs[setNum].add(edge[1])
                continue
                
            elif (edge[0] in connected_nodes and edge[1] in connected_nodes):
                setNum0 = setNum = self.findSet(graphs, edge[0])
                setNum1 = setNum = self.findSet(graphs, edge[1])
                
                if (setNum0 == setNum1):
                    return edge
                set0 = graphs[setNum0]
                set1 = graphs[setNum1]
                set2 = set0.union(set1)
                
                del graphs[max(setNum0, setNum1)]
                del graphs[min(setNum0, setNum1)]
                graphs.append(set2)
            
        return "Should not be here"
                