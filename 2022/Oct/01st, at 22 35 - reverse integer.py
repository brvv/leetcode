class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)
        number = number[::-1]
        res = 0
        if number[-1] == "-":
            res = int("-" + (number[:-1]))
        else:
            res =  int(number)
        
        if -(2**31) < res < (2**31) -1:
            return res
        else:
            return 0