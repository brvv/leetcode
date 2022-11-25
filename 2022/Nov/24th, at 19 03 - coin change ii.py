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
        return coinChangeRec(len(coins)-1, amount)