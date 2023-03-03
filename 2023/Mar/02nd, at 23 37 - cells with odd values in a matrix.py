class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_inc = [i[0] for i in indices]
        col_inc = [i[1] for i in indices]

        rows = [0 for i in range(m)]
        cols = [0 for i in range(n)]

        for inc in row_inc:
            rows[inc] += 1

        for inc in col_inc:
            cols[inc] += 1

        res = 0

        for col_i in range(len(cols)):
            for row_i in range(len(rows)):
                final = cols[col_i] + rows[row_i]
                res += final % 2
        return res
        