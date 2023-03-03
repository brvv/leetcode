class Solution:
    def countTriples(self, n: int) -> int:
        vals = [i ** 2 for i in range(1, n + 1)]
        vals_set = set(vals)
        res = 0
        for i in range(len(vals)):
            for j in range(i, len(vals)):
                if ( vals[i] + vals[j] ) in vals_set:
                    res += 1
        return res * 2