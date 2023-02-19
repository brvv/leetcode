class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] = shifts[i] + shifts[i + 1]

        res = []
        print(shifts)
        for i, letter in enumerate(s):
            curr_char = ord(letter) - ord('a')
            shift = shifts[i] % 26
            new_char = (curr_char + shift) % 26

            res.append(chr(new_char + ord('a')))

        return ''.join(res)