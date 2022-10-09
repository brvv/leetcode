class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for _ in temperatures]
        
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                lower = stack.pop()
                days_diff = i - lower[1]
                ans[lower[1]] = days_diff
            
            stack.append([temp, i])
        return ans