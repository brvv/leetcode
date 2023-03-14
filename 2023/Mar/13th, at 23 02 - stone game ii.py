class Solution:
    def stoneGameII(self, piles: List[int]) -> int:  
        cache = {}

        def dfs(start=0, M=1, turn=0):
            if start >= len(piles):
                return 0

            subproblem = tuple([start, M, turn])
            if subproblem in cache:
                return cache[subproblem] 


            #alice turn
            if turn == 0:
                alice = []
                for X in range(1, 2 * M  + 1):
                    pile = piles[start : start + X]
                    pileSum = sum(pile)
                    newM = max(M, X)
                    alice.append(pileSum + dfs(start + X, newM, 1))
                cache[subproblem] = max(alice)
                return cache[subproblem] 

        
            #bob turn
            else:
                alice = []
                for X in range(1, 2 * M  + 1):
                    pile = piles[start : start + X]
                    pileSum = sum(pile)
                    newM = max(M, X)
                    alice.append(dfs(start + X, newM, 0))
                cache[subproblem] = min(alice)
                return cache[subproblem]
        return dfs()