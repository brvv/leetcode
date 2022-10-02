class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(brackets, n, numOpen=0, numClosed=0):
            if numOpen == numClosed == n:
                ans.append(brackets)
                return
            
            if (numOpen < n):
                dfs(brackets + "(", n, numOpen + 1, numClosed)
                
            if (numOpen > numClosed and numClosed < n):
                dfs(brackets + ")", n, numOpen, numClosed + 1)
        
        dfs("", n, 0, 0)
        return ans