class Solution:
    def getMin(self, matrix, coord):
        if coord[1] - 1 < 0 or coord[0] - 1 < 0:
            return matrix[coord[0]][coord[1]]
        
        #val1 = matrix[coord[0]][coord[1]]
        val2 = int(matrix[coord[0]][coord[1] - 1])
        val3 = int(matrix[coord[0]-1][coord[1]])
        val4 = int(matrix[coord[0]-1][coord[1]-1])

        
        return min(val2, val3, val4)
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        new_matrix = [[int(item) for item in row] for row in matrix]
        max_val = 0
        
        for row_i in range(1, len(matrix)):
            for col_i in range(1, len(matrix[row_i])):
                min_val = self.getMin(new_matrix, [row_i, col_i])
                current_val = new_matrix[row_i][col_i]
                
                if current_val == 1 and min_val > 0:
                    new_matrix[row_i][col_i] = 1 + min_val
                    max_val = max(max_val, 1 + min_val)
                
        for row in new_matrix:
            for item in row:
                max_val = max(max_val, item)
        
       
  
        return max_val * max_val