class Solution:
    def isInCircle(self, point, circle):
        return circle[2] >= (((point[0]-circle[0])**2 + (point[1]-circle[1])**2)**0.5)
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0 for i in queries]
        
        for point in points:
            for c_i, circle in enumerate(queries):
                if self.isInCircle(point, circle):
                    ans[c_i] += 1
        return ans