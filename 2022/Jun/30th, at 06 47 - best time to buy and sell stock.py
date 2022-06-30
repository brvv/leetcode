class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        pointer1 = 0
        pointer2 = 1
        max_profit = 0
        
        while(pointer2 < len(prices)):
            price1 = prices[pointer1]
            price2 = prices[pointer2]
            
            if price1 <= price2:
                profit = price2 - price1
                max_profit = max(profit, max_profit)
            else:
                pointer1 = pointer2
            pointer2 += 1
        return max_profit
                