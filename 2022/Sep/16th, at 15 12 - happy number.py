class Solution:
    def isHappy(self, n: int) -> bool:
        tried_nums = []
        tried_nums.append(n)
        
        str_num = str(n)
        
        
        while (str_num != "1"):
            new_num = 0
            for char in str_num:
                new_num += int(char) ** 2
            
            if (new_num in tried_nums):
                return False
            tried_nums.append(new_num)
            str_num = str(new_num)
        return True
        