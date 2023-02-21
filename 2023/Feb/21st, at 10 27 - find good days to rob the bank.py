class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        increasing = [1 for i in security]
        decreasing = [1 for i in security]

        res = []

        for i in range(1, len(increasing)):
            increasing[i] = increasing[i-1] + 1 if security[i-1] >= security[i] else 1
        

        for i in range(len(decreasing) - 2, -1 , -1):
            decreasing[i] = decreasing[i+1] + 1 if security[i+1] >= security[i] else 1
        
        for i in range(len(security)):
            if increasing[i] > time and decreasing[i] > time:
                res.append(i)
        
        return res

'''

[5,3,3,3,5,6,2]
inc
 1 2 3 4 1 1 2

 dec
 1 5 4 3 2 1 1 




'''