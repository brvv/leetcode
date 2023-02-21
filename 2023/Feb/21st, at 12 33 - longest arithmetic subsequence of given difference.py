class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seq = {}
        used_vals = set({})

        for elem in arr:
            if (elem - difference) in seq:
                seq[elem] = seq[elem - difference] + 1
                if elem != (elem - difference):
                    del seq[elem - difference]
            elif elem not in seq:
                seq[elem] = 1
        print(seq)
        return max(seq.values())
            
                