class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        #recursive dynamic programming solution
        def dfs(text1, text2, index1=0, index2=0):
            if index1 >= len(text1) or index2>=len(text2):
                return 0
            
            if tuple([index1, index2]) in cache:
                return cache[tuple([index1, index2])]
            
            letter1 = text1[index1]
            letter2 = text2[index2]
            
            if letter1 == letter2:
                val = 1 + dfs(text1, text2, index1 + 1, index2 + 1)
            else:
                val = max(dfs(text1, text2, index1 + 1, index2), dfs(text1, text2, index1, index2 + 1))
            cache[tuple([index1, index2])] = val
            return cache[tuple([index1, index2])]
        
        #table-based dynamic programming solution
        def dpLCS(text1, text2):
            # text1 on vertical axis and text2 on horizontal
            table = [[0 for char2 in text2] for char1 in text1]
            
            for row_i, row in enumerate(table):
                for col_i, item in enumerate(row):
                    letter1 = text1[row_i]
                    letter2 = text2[col_i]
                    
                    top = table[row_i-1][col_i] if row_i-1 >= 0 else 0
                    left = table[row_i][col_i - 1] if col_i - 1 >= 0 else 0
                    topleft = table[row_i-1][col_i-1] if col_i -1 >= 0 and row_i >= 0 else 0
                    
                    if letter1 == letter2:
                        table[row_i][col_i] = 1 + topleft
                    else:
                        table[row_i][col_i] = 0 + max(top, left)
            return table[-1][-1]
                    
            
        return dpLCS(text1, text2)