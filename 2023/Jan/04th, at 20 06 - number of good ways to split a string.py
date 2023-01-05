class Solution:
    def numSplits(self, s: str) -> int:
        leftDistinct = [0 for i in s]
        leftDistinct[0] = 1

        letters = {}
        letters[s[0]] = 0

        for i in range(1, len(s)):
            letter = s[i]
            leftDistinct[i] = leftDistinct[i - 1]
            if letter not in letters:
                leftDistinct[i] += 1
                letters[letter] = i

        rightDistinct = [0 for i in s]
        rightDistinct[-1] = 1

        letters = {}
        letters[s[-1]] = 0

        for i in range(len(s) -2, -1,-1):
            letter = s[i]
            rightDistinct[i] = rightDistinct[i + 1]
            if letter not in letters:
                rightDistinct[i] += 1
                letters[letter] = i
        good_ways = 0

        for i in range(0, len(s) - 1):
            if leftDistinct[i] == rightDistinct[i + 1]:
                good_ways += 1
        return good_ways