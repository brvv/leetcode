class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [None for i in prices]
        
        for i in range(len(prices)-1, -1, -1):
            if i + 1 < len(prices):
                profits[i] = max(profits[i + 1], prices[i])
            else:
                profits[i] = prices[i]
                
        costs = [None for i in prices]
        
        for i in range(0, len(prices)):
            if i-1 >= 0:
                costs[i] = min(costs[i-1], prices[i])
            else:
                costs[i] = prices[i]
                
        sums = []
        
        for buy_price, sell_price in zip(costs[:-1:], profits[1::]):
            sums.append(sell_price - buy_price)
            
        if len(sums) <= 0:
            return 0
        
        return max(max(sums), 0)
            
                