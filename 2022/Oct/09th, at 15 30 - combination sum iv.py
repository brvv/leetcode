class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums_set = set(nums)
        val_dic = {0 : 1}
        

        for i in range(1, target + 1):   
            val_dic[i] = 0
            
            for n in nums:
                val_dic[i] += val_dic.get(i - n, 0)
        return val_dic[target]
                
        