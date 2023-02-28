class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = 1 + s_dict.get(char, 0)

        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)

        for char in string.ascii_lowercase:
            if char in s_dict and char in t_dict:
                res += abs(s_dict[char] - t_dict[char])
            elif char in s_dict:
                res += s_dict[char]
            elif char in t_dict:
                res += t_dict[char]
        
        return res