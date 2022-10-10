class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = ([x, y, -(x ** 2 + y ** 2)] for [x, y] in points)
        points = defaultdict(list)
        maxheap = []
        
        
        for [x, y, distance] in distances:
            points[distance].append([x, y])
            maxheap.append(distance)
            
        heapq.heapify(maxheap)
        
        while len(maxheap) > k:
            distance = heapq.heappop(maxheap)
            
            points[distance].pop()
            
            if len(points[distance]) == 0:
                del points[distance]
        
        res = []
        for lst in points.values():
            for val in lst:
                res.append(val)
        return res
            
        
        