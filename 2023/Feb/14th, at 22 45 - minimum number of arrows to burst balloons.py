class Solution:
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points)
        arrows = 0
        first_balloon = 0

        while first_balloon < len(points):
            #pop first balloon
            [first_start, first_end] = sorted_points[first_balloon]
            first_balloon += 1
            arrows += 1

            while first_balloon < len(points) and sorted_points[first_balloon][0] <= first_end:
                first_end = min(first_end, sorted_points[first_balloon][1])
                first_balloon += 1

        return arrows

