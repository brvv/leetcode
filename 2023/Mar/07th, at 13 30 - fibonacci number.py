class Solution(object):
    fib_dict = {0:0, 1:1}
    def fib(self, n):
        n1, n2 = 0, 1
        if n <= 1:
            return [0, 1][n]
        
        for i in range(2, n+1):
            n3 = n1 + n2
            n1, n2 = n2, n3
        return n3