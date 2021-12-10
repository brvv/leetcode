class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {'I' : 1,
                     'V' : 5,
                     'X' : 10,
                     'L' : 50,
                     'C' : 100,
                     'D' : 500,
                     'M' : 1000}
        overwrite = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900,
        }
        
        decimal_result = 0
        i = 0
        while (i<len(s)):
            step_val = 0
            if i + 1 < len(s) and s[i:i+2] in overwrite.keys():
                step_val = overwrite[s[i:i+2]]
                i += 1
            else:
                step_val = conversion[s[i]]
            
            decimal_result += step_val
            i += 1
        return decimal_result