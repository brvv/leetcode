class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        res = []

        def back(curr_digit, max_len, curr_seq=''):
            if len(curr_seq) == max_len:
                if len(curr_seq) > 0:
                    res.append(curr_seq)
                return
            

            for letter in mapping[int(digits[curr_digit])]:
                back(curr_digit + 1, max_len, curr_seq + letter)
        back(0, len(digits))
        return res