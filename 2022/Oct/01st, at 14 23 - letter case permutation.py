class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        nums = set({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
        res = []
        
        def dfs(string):
            if len(string) >= len(s):
                res.append(string)
                return
            else:
                current_char_num = len(string)
                current_char = s[current_char_num]

                if current_char in nums:
                    dfs(string + current_char)
                else:
                    lower = current_char.lower()
                    upper = current_char.upper()

                    dfs(string + lower)
                    dfs(string + upper)
                
        dfs("")
        return res
        
        