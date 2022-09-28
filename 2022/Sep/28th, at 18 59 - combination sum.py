class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        current_subset = []
        
        def dfs(i, current_subset_sum=0):
            

            if current_subset_sum > target:
                return
            elif current_subset_sum == target:
                combinations.append(current_subset.copy())
                return
            if i >= len(candidates):
                return
            
            for n in range(0, len(candidates)-i):

                current_subset.append(candidates[i + n])
                current_subset_sum += candidates[i + n]
                dfs(i + n, current_subset_sum)
                current_subset.pop()
                current_subset_sum -= candidates[i + n]
            
        dfs(0)
        return combinations
        
            