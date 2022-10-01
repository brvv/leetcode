class Solution:
    def setRowNones(self, matrix, row_num):
        for col_num in range(len(matrix[row_num])):
            item = matrix[row_num][col_num]
            
            if (item == 0):
                matrix[row_num][col_num] = None
                self.setColNones(matrix, col_num)
            else:
                matrix[row_num][col_num] = None
            
    def setColNones(self, matrix, col_num):
        for row_num in range(len(matrix)):
            item = matrix[row_num][col_num]
            
            if (item == 0):
                matrix[row_num][col_num] = None
                self.setRowNones(matrix, row_num)
            else:
                matrix[row_num][col_num] = None
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        for row_i, row in enumerate(matrix):
            for col_i, item in enumerate(row):
                if item == 0:
                    matrix[row_i][col_i] = None
                    self.setRowNones(matrix, row_i)
                    self.setColNones(matrix, col_i)
                    
        for row_i, row in enumerate(matrix):
            for col_i, item in enumerate(row):
                if item == None:
                    matrix[row_i][col_i] = 0