class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        filled = 0
        diff = [c - r for c, r in zip(capacity, rocks)]

        s_diff = sorted(diff)



        for space in s_diff:
            if space <= additionalRocks:
                additionalRocks -= space
                filled += 1
        
        return filled