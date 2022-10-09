class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        end = rows * cols - 1
        
        while start <= end:
            middle = (start + end) // 2
            
            col_coord = middle % cols
            row_coord = (middle - col_coord)//cols
            
            val = matrix[row_coord][col_coord]
            
            if val == target:
                return True
            elif val < target:
                start = middle + 1
            else:
                end = middle - 1
        return False
