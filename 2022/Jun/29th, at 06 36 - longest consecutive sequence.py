class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        maxSeq = 1
        
        if not nums:
            return 0
        
        for num in nums:
            dic[num] = True
        
        
        
        for num in dic.keys():
            if dic[num]:
                downStep = 1
                upStep = 1
                seqSize = 1
                
                while(True):
                    downNum = num-downStep
                    upNum = num + upStep
                    
                    
                    if (downNum) in dic and dic[downNum]:
                        dic[downNum] = False
                        downStep += 1
                        seqSize += 1
                        continue
                    
                    if (upNum) in dic and dic[upNum]:
                        dic[upNum] = False
                        upStep += 1
                        seqSize += 1
                        continue
                        
                    break
                
                if seqSize > maxSeq:
                    maxSeq = seqSize
        return maxSeq
                
                
                        