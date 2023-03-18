class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []

        for col_i in range(len(matrix[0])):
            res.append([])
            for row_i in range(len(matrix)):
                res[-1].append(matrix[row_i][col_i])
        
        return res