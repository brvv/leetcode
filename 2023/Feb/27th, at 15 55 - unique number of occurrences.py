class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # number to occurency of that number
        unique = {}
        for number in arr:
            if number not in unique:
                unique[number] = 1
            else:
                unique[number] += 1

        # occurency of that number to occurency of its occurency
        occurrences = {}

        for num in unique:
            occurency = unique[num]
            if occurency not in occurrences:
                occurrences[occurency] = 1
            else:
                return False
        return True
            