class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        min_letter = None
        min_diff = 1000000000000

        for letter in letters:
            diff = ord(letter) - ord(target)

            if diff >= 1 and diff < min_diff:
                min_letter = letter
                min_diff = diff

        if min_letter == None:
            return letters[0]

        return min_letter