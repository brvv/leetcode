class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def rowMinFalling():
            prev_row = None
            
            for row_i, row in enumerate(matrix):
                new_row = [item for item in row]
                for col_i, cost in enumerate(matrix[row_i]):
                    if row_i == 0:
                        continue
                    left, top, right = 0, 0, 0
                    left = prev_row[col_i - 1] if col_i - 1 >= 0 else 100000000
                    top = prev_row[col_i]
                    right = prev_row[col_i + 1] if col_i + 1 < len(prev_row) else 10000000000
                    
                    new_row[col_i] = cost + min(left, top, right)
                
                prev_row = new_row
                print(prev_row)
            return min(prev_row)
        return rowMinFalling()