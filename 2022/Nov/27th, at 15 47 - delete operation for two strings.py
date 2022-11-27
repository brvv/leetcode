class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcsTable(str1, str2):
            table = [[0 for c2 in str2] for c1 in str1]
            
            
            for row_i in range(len(table)):
                row = table[row_i]
                for col_i in range(len(row)):
                    left = table[row_i][col_i - 1] if col_i > 0 else 0
                    top = table[row_i-1][col_i] if row_i > 0 else 0
                    left_top = table[row_i-1][col_i-1] if col_i > 0 and row_i > 0 else 0

                    c1 = str1[row_i]
                    c2 = str2[col_i]
                    
                    if c1 == c2:
                        table[row_i][col_i] = left_top + 1
                    else:
                        table[row_i][col_i] = max(left, top)
            return table[-1][-1]
        
        lcs_size = lcsTable(word1, word2)
        
        steps1 = len(word1) - lcs_size
        steps2 = len(word2) - lcs_size
        
        return steps1 + steps2