class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for par in s:
            stack.append(par)

            while len(stack) >= 2 and (stack[-1] == ')' and stack[-2] == '('):
                stack.pop()
                stack.pop()
        return len(stack)

