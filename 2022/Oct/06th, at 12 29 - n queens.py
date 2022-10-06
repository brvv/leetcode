class Solution:
    def getPositiveDiagonal(self, coord):
        return sum(coord)
    
    def getNegativeDiagonal(self, coord, n):
        diff = coord[1] - coord[0]
        return (n - 1 - diff)
    
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        def dfs(max_rows, row_num = 0, cols = [], skip_cols=set({}), skipd_positive=set({}), skipd_negative=set({})):
            if row_num >= max_rows:
                res = []
                for row_i, col_i in zip(range(max_rows), cols):
                    # col_i = 3   . . . Q
                    prefix = '.'  * col_i
                    postfix = '.' * (max_rows - 1 - col_i)
                    res.append(prefix + 'Q' +  postfix)
                ans.append(res)
            
            
            for i in range(max_rows):
                if i not in skip_cols:
                    i_positive_diag = self.getPositiveDiagonal([row_num, i])
                    i_negative_diag = self.getNegativeDiagonal([row_num, i], max_rows)
                    
                    if i_positive_diag not in skipd_positive and i_negative_diag not in skipd_negative:
                        dfs(max_rows, row_num + 1, cols + [i], skip_cols.union([i]), skipd_positive.union([i_positive_diag]), skipd_negative.union([i_negative_diag]))
        
        dfs(n)
        
        
        return ans