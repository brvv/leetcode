class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        choices = set({})
        res=set({})
        
        for i, val in enumerate(nums):
            choices.add(tuple([val, i]))
            
        def dfs(permutation=[], choices=[]):
            if len(choices) == 0:
                res.add(tuple(permutation))
                return
            
            
            for choice in choices:
                dfs(permutation + [choice[0]], choices - {choice})
        dfs([], choices)
        return res
            
                