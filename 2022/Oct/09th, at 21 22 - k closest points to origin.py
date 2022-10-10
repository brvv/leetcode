class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = ([x, y, (x ** 2 + y ** 2)] for [x, y] in points)
        points = defaultdict(list)
        maxheap = []
        
        
        for [x, y, distance] in distances:
            points[distance].append([x, y])
            maxheap.append(distance)
            
        heapq.heapify(maxheap)
        res = []
        for i in range(k):
            distance = heapq.heappop(maxheap)
            
            point = points[distance].pop()
            res.append(point)

        
        return res
            
        
        