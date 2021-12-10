class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_par = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for i in range(len(s)):
            if s[i] not in matching_par.keys():
                stack.append(s[i])
            else:
                if i == 0 or len(stack) == 0 or stack[-1] != matching_par[s[i]]:
                    return False
                stack.pop()
        return len(stack) == 0