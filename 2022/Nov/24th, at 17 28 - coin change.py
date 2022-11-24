class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        #recursive approach
        def coinChangeRec(index, amount):
            if index < 0 or amount < 0:
                return 1000000000
            
            if amount == 0:
                return 0
            
            subproblem = tuple([index, amount])
            
            if subproblem in dp:
                return dp[subproblem]
            
            take_same_coin = 1 + coinChangeRec(index, amount - coins[index])
            move_to_next = 0 + coinChangeRec(index - 1, amount)
            
            dp[subproblem] = min(take_same_coin, move_to_next)
            return dp[subproblem]
        
        
        #table approach
        def coinChangeTable(index, amount, coins):
            if amount == 0:
                return 0
            
            BIG_INT = 100000000000000
            table = [[BIG_INT for j in range(amount+1)] for i in range(index+1)]
            
            for r_i in range(index + 1):
                table[r_i][0] = 0
                
            for coin_i, coin in enumerate(coins):
                if coin <= amount:
                    table[coin_i][coin] = 1
            
            for row_i in range(0, len(table)):
                row = table[row_i]
                for col_i, item in enumerate(row):
                    if item == BIG_INT:
                        take_same_coin = BIG_INT
                        move_to_next = BIG_INT
                        
                        if (row_i-1>=0):
                            move_to_next = table[row_i - 1][col_i]
                        
                        if col_i >= coins[row_i]:
                            take_same_coin = 1 + table[row_i][col_i - coins[row_i]]
                        
                        
                        
                        table[row_i][col_i] = min(take_same_coin, move_to_next, table[row_i][col_i])    
            return table[-1][-1]
        ans = coinChangeTable(len(coins)-1, amount, coins)
        if ans == 100000000000000:
            return -1
        return ans
        
        
            