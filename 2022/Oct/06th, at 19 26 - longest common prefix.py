class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_string_len = min([len(s) for s in strs])
        
        for i in range(min_string_len):
            char = strs[0][i]
            
            for s in strs:
                if s[i] != char:
                    return prefix
            
            prefix += char
        return prefix