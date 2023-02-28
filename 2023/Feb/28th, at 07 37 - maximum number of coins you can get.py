class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        s_piles = sorted(piles)
        start_index = 0
        end_index = len(piles)-2
        res = 0

        while start_index < end_index:
            item = s_piles[end_index]
            res += item
            start_index += 1
            end_index -=2 
        return res