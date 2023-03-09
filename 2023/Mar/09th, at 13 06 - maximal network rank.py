class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        
        max_rank = 0
        for first_node in graph:
            first_rank = len(graph[first_node])

            for second_node in graph:
                if second_node == first_node:
                    continue
                second_rank = len(graph[second_node])
                modifier = -1 if second_node in graph[first_node] else 0
                max_rank = max(max_rank, first_rank + second_rank + modifier)
        
        return max_rank


