class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if min(len(firstList), len(secondList)) == 0:
            return []

        i1 = 0
        i2 = 0
        areIntersecting = False
        res = []

        while i1 < len(firstList) and i2 < len(secondList):
            ptr1 = firstList[i1]
            ptr2 = secondList[i2]

            if ptr1[0] <= ptr2[0] <= ptr1[1] or ptr2[0] <= ptr1[0] <= ptr2[1]:
                res.append([max(ptr1[0], ptr2[0]), min(ptr1[1], ptr2[1])])

            if ptr1[1] < ptr2[1]:
                i1 += 1
                continue

            if ptr2[1] < ptr1[1]:
                i2 += 1
                continue

            i1 += 1
            i2 += 1

        return res 

