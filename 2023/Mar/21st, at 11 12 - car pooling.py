class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickup = defaultdict(int)
        dropoff = defaultdict(int)

        for passengers, pick, drop in trips:
            pickup[pick] += passengers
            dropoff[drop] += passengers

        occupancy = 0
        
        for curr in range(1000 + 1):
            if curr in dropoff:
                occupancy = max(0, occupancy - dropoff[curr])
            
            if curr in pickup:
                occupancy += pickup[curr]
            
            if occupancy > capacity:
                return False
        
        return True
            



