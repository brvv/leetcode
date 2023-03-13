class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #alice wins if her sum is bigger than half of sum of piles
        stoneSum = sum(piles)
        cache = {}

        first = 0
        last = len(piles) - 1

        def dfs(alSum, move, first, last):
            print(alSum, move, first, last)
            if first >= last:
                return 0

            pile1 = piles[first]
            pile2 = piles[last]

            subproblem = tuple([first, last])
            if subproblem in cache:
                return cache[subproblem]

            if move % 2 == 0:
                # alice move
                #pick first 
                p1 = pile1 + dfs(alSum, move + 1, first + 1, last)
                # pick last
                p2 = pile2 + dfs(alSum, move + 1, first, last - 1)
                cache[subproblem] = max(p1, p2)
                return cache[subproblem]
            else:
                # bob move
                # pick first
                p1 = dfs(alSum, move + 1, first + 1, last)
                # pick last
                p2 = dfs(alSum, move + 1, first, last - 1)

                #bob wants to minimize alice score

                cache[subproblem] = min(p1, p2)
                return cache[subproblem]
        res =  dfs(0, 0, first, last)
        return res > stoneSum // 2
