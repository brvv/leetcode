class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        stone_sum = sum(stoneValue)
        target = stone_sum / 2

        cache = {}

        def dfs(start=0, turn=0):
            if start >= len(stoneValue):
                return 0

            subproblem = tuple([start, turn])
            if subproblem in cache:
                return cache[subproblem]

            #Alice turn
            if turn == 0:
                alice = []
                for i in range(1, 4):
                    val = sum(stoneValue[start : start + i])
                    max_alice = val + dfs(start + i, 1)
                    alice.append(max_alice)
                cache[subproblem] = max(alice)



            #Bob turn
            else:
                alice = []
                for i in range(1, 4):
                    val = sum(stoneValue[start : start + i])
                    max_alice = dfs(start + i, 0)
                    alice.append(max_alice)
                cache[subproblem] = min(alice)
            return cache[subproblem]


        res = dfs()
        
        if res < target:
            return 'Bob'
        elif res == target:
            return 'Tie'
        else:
            return 'Alice'
