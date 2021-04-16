class Solution(object):
    fib_dict = {0:0, 1:1}
    def fib(self, n):
        if n in self.fib_dict:
            return self.fib_dict[n]
        else:
            self.fib_dict[n] = self.fib(n-1) + self.fib(n-2)
            return self.fib_dict[n]
        