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
        
        ans = coinChangeRec(len(coins) - 1, amount)
        if ans == 1000000000:
            return -1
        return ans
            