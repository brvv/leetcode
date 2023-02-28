class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodes = defaultdict(list)
        checked = set({})
        checked.add(0)

        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        def minTimeRec(node, curr_depth):
            children_time = 0

            for child in nodes[node]:
                if child not in checked:
                    checked.add(child)
                    child_time = minTimeRec(child, curr_depth + 1)
                    children_time += child_time
            
            curr_time = 1 if children_time > 0 or hasApple[node] else 0 
            res = children_time + curr_time

            if node == 0:
                if children_time == 0:
                    return 0
                else:
                    return (res-1) * 2
            return res

        return minTimeRec(0, 0)

            
            
        
