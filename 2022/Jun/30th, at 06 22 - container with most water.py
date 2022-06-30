class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(height) - 1
        max_area = 0
        
        while (pointer1 < pointer2):
            height1 = height[pointer1]
            height2 = height[pointer2]
            area = min(height1, height2) * (pointer2-pointer1)
            
            max_area = max(area, max_area)
            
            if height1 < height2:
                pointer1 += 1
            elif height2 < height1:
                pointer2 -= 1
            else:
                point1_2 = pointer1 + 1
                point2_2 = pointer2 - 1
                
                height1_2 = height[point1_2]
                height2_2 = height[point2_2]
                
                diff1 = height1 - height1_2
                diff2 = height2 - height2_2
                
                if diff1 < diff2:
                    pointer1 += 1
                else:
                    pointer2 -= 1
        return max_area
                    