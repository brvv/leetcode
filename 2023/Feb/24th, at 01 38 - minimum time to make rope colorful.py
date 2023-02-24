#min heap sliding window? n log n

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        start_index = 0
        end_index = 0
        start_balloon = colors[start_index]

        total_cost = 0

        heap = []

        while start_index < len(colors) - 1:
            start_balloon = colors[start_index]
            end_index += 1
            next_balloon = colors[end_index]

            if next_balloon != start_balloon:
                start_index += 1
                end_index = start_index
                continue

            heap = []
            heapq.heappush(heap, neededTime[start_index])
            while next_balloon == start_balloon:

                heapq.heappush(heap, neededTime[end_index])
                end_index += 1

                if end_index >= len(colors):
                    break
                next_balloon = colors[end_index]
                

            
            start_index += len(heap)

            while len(heap) != 1:
                print(start_index, end_index)

                total_cost += heapq.heappop(heap)
        return total_cost



            