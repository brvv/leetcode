class Solution:
    def __init__(self):
        self.maxscore = 0
        self.res = []
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        ans = []

        def dfs(numArrows, index = 11, score=0):
            if index < 0:
                if score > self.maxscore:
                    self.maxscore = score
                    self.res = ans.copy()
                    self.res[0] += numArrows
                return 0

            alice = aliceArrows[index]

            take = 0
            #bob skips the score
            ans.append(0)
            skip = dfs(numArrows, index - 1, score)
            ans.pop()
            #bob takes the score
            if numArrows > alice:
                ans.append(alice + 1)
                take = dfs(numArrows - (alice + 1), index - 1, score + index)
                ans.pop()

        dfs(numArrows)
        return self.res[::-1]