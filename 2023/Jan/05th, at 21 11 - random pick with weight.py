class Solution:

    def __init__(self, w: List[int]):
        self.sums = []
        self.sums.append(w[0])

        for i in range(1, len(w)):
            self.sums.append(self.sums[i-1] + w[i])



    def pickIndex(self) -> int:
        rand_val = random.randint(1, self.sums[-1])

        return bisect_left(self.sums, rand_val)
        


# 1 3 5
# 1 4 9
# 0 - 4
# 1 2 3 4 5 6 7 8 9 
# 0 2 2 2 3 3 3 3 3