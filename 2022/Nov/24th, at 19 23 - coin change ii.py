class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def coinChangeRec(index, amount):
            if amount < 0:
                return 0
            
            if index < 0:
                if amount == 0:
                    return 1
                return 0
            
            subproblem = tuple([index, amount])
            if subproblem in dp:
                return dp[subproblem]
            
            take_current = coinChangeRec(index, amount - coins[index])
            go_next = coinChangeRec(index - 1, amount)
            
            dp[subproblem] = take_current + go_next
            return dp[subproblem]
        
        def coinChangeTable(coins, amount):
            table = [[0 for _ in range(amount + 1)] for c in coins]
            
            table[0][0]=1
            
            for row_i in range(len(table)):
                row = table[row_i]
                for col_i in range(len(row)):
                    ways = table[row_i][col_i]
                    current_coin = coins[row_i]
                    amount = col_i
                    
                    if row_i > 0:
                        table[row_i][col_i] = table[row_i-1][col_i]
                    
                    if amount - current_coin >= 0:
                        #take more of current coin
                        table[row_i][col_i] += table[row_i][col_i-current_coin]
                    
            return table[-1][-1]
        
        return coinChangeTable(coins, amount)