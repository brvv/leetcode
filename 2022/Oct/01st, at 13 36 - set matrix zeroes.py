class Solution:
    def setRowZeroes(self, matrix, row_num):
        for col_num in range(len(matrix[row_num])):
            matrix[row_num][col_num] = 0
            
    def setColZeroes(self, matrix, col_num):
        for row_num in range(len(matrix)):
            matrix[row_num][col_num] = 0
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack = []
        
        for row_i, row in enumerate(matrix):
            for col_i, item in enumerate(row):
                if item == 0:
                    stack.append([row_i, col_i])
                    
        while stack:
            coords = stack.pop()
            
            self.setRowZeroes(matrix, coords[0])
            self.setColZeroes(matrix, coords[1])
        