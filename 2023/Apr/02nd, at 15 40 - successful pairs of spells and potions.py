class Solution:


    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        s_potions = sorted(potions)
        ans = []
        
        for spell in spells:
            target = success / spell
            index = bisect_left(s_potions, target)
            ans.append(len(potions) - index)
        return ans