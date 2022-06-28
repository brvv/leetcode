class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # exp [1 2 3 4 ]
        # asc [ 1 2 6 24]
        # dec [ 24 24 12 4]
        # res [ dec[1], asc[0] * dec[2], asc[1] * dec[3], asc[2]]
        
        asc = []
        for i, item in enumerate(nums):
            if i > 0:
                asc.append(item * asc[i-1])
            else:
                asc.append(item)
                
        dec = [None for _ in nums]
        
        for i in range(len(nums)-1, -1,-1):
            if i == (len(nums)-1):
                dec[i] = nums[i]
            else:
                dec[i] = dec[i+1] * nums[i]
        
        res = [None for _ in nums]
        
        res[0] = dec[1]
        res[-1] = asc[-2]
        
        for i in range(1, len(res)-1):
            res[i] = asc[i-1] * dec[i+1]
    
        return res