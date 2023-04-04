class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = defaultdict(int)
        
        for num in nums:
            dic[num] += 1
        
        ans = []
        while True:
            ans.append([])
            to_delete = []
            
            for key in dic:
                if dic[key] > 0:
                    ans[-1].append(key)
                    dic[key] -= 1
                
                if dic[key] == 0:
                    to_delete.append(key)
            
            for key in to_delete:
                del dic[key]
            
            if len(dic) == 0:
                break
        return ans
                    
        