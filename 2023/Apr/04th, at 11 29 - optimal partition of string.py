class Solution:
    def partitionString(self, s: str) -> int:
        part = set({})
        parts = 1

        for letter in s:
            if letter not in part:
                part.add(letter)
            else:
                parts += 1
                part = set({})
                part.add(letter)
        return parts