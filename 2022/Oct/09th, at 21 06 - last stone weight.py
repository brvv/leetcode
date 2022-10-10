class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-s for s in stones]
        
        heapq.heapify(stones_heap)
        
        while len(stones_heap) > 1:
            stone1 = heapq.heappop(stones_heap)
            stone2 = heapq.heappop(stones_heap)
            
            if stone1 == stone2:
                continue
            #100 and 80: 100 - 80 = 20; -100 - -80 = -20
            winner = stone1-stone2 if stone1 < stone2 else stone2-stone1
            heapq.heappush(stones_heap, winner)
        
        
        return -stones_heap[0] if stones_heap else 0