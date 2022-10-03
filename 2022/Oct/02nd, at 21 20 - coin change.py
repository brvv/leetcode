class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coin_amounts = {}
        
        coin_amounts[0] = 0
        coin_dic = {}
        for coin in coins:
            coin_amounts[coin] = 1
            
        for i in range(1, amount + 1):
            if(i in coin_amounts):
                continue
            
            min_amount = None
            
            for coin in coins:
                target = i - coin
                
                if target < 0:
                    continue
                
                prev_amount = coin_amounts[target]
                
                if prev_amount == -1:
                    continue
                    
                actions = coin_amounts[target] + 1    
                
                if min_amount is None or actions < min_amount:
                    min_amount = actions
            
            if min_amount is None:
                coin_amounts[i] = -1
            else:
                coin_amounts[i] = min_amount
        return coin_amounts[amount]