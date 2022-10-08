class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
         
        for char in s1:
            dic1[char] = 1 + dic1.get(char, 0)
            
        for i in range(0, len(s2) - len(s1) + 1):
            s2_slice = s2[i : i + len(s1)]
            
            slice_dic = {}

            for char in s2_slice:
                slice_dic[char] = 1 + slice_dic.get(char, 0)
                
            if slice_dic == dic1:
                print(s2_slice, i, i + len(s1))
                return True
        return False
            