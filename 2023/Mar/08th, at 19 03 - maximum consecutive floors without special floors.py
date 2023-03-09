class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        floors = [ bottom - 1 ] + sorted(special) + [ top + 1 ]

        max_gap = 0

        for i in range(1, len(floors)):
            max_gap = max(max_gap, floors[i] - floors[i - 1] - 1)
        
        return max(0, max_gap)