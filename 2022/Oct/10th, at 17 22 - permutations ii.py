class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        choices = {}
        for num in nums:
            choices[num] = 1 + choices.get(num, 0)
            
        res=[]
            
        def dfs(maxlevel, choices, permutation=[]):
            if len(permutation) == maxlevel:
                res.append(permutation)
                return
            
            
            for choice in choices:
                if choices[choice] > 0:
                    choices[choice] -= 1
                    dfs(maxlevel, choices, permutation + [choice])
                    choices[choice] += 1

        dfs(len(nums), choices)
        return res
            
                