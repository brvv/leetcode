class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        
        for item in nums:
            if item not in dups:
                dups[item] = True
            else:
                return True
        return False