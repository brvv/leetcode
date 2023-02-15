class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        sorted_h = sorted(horizontalCuts)
        sorted_v = sorted(verticalCuts)
        sorted_v.append(w)
        sorted_h.append(h)

        start = 0
        max_height = 0
        for i in range(len(sorted_h)):
            cut = sorted_h[i]
            max_height = max(cut - start, max_height)
            start = cut

        start = 0
        max_width = 0
        for i in range(len(sorted_v)):
            cut = sorted_v[i]
            max_width = max(cut - start, max_width)
            start = cut


        return (max_height * max_width) % (10**9 + 7)