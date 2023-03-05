class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])

        while len(res) < numRows:
            new_row = []
            new_row.append(1)
            for i in range(0, len(res[-1]) - 1):
                new_row.append(res[-1][i] + res[-1][i + 1])
            new_row.append(1)
            res.append(new_row)
        return res