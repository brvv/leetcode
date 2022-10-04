class Solution:
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numsSum = sum(nums)
        
        if numsSum % k != 0:
            return False
        
        subSetSum = numsSum / k
        newNums = nums.copy()
        cache = {}
        
        subSets = []
        
        def findIndeces(nums, targetSum, startIndex=0, setSum=0,  indices=set({}),  exclude=set({})):
            if setSum == targetSum:
                subSets.append(indices)
                return None
            elif setSum > targetSum:
                return None
            
            
            for i in range(startIndex, len(nums)):
                if i in exclude or i in indices:
                    continue
                
                ans = findIndeces(nums, targetSum, i, setSum + nums[i], indices.union({i}), exclude)
                
                if ans is not None:
                    return ans
            return None
                
        
        findIndeces(nums, subSetSum)
        
        
        def dfs(sets, startIndex, numSets, exclude=set({})):
            if numSets == 0:
                return True
            
            for i in range(startIndex, len(sets)):
                currentSet = sets[i]
                
                if (len(currentSet.intersection(exclude)) == 0):
                    val = dfs(sets, i, numSets-1, exclude.union(currentSet))
                    
                    if val == True:
                        return True
            return False
        
        return dfs(subSets, 0, k)
        
                
        
        
        