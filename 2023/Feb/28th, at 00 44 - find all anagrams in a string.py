class Solution:
    def checkEq(self, d1, d2):
        for key in d2:
            if key not in d1 or d1[key] != d2[key]:
                return False
        return True

    def findAnagrams(self, s: str, p: str) -> List[int]:
        frame_size = len(p)
        if frame_size > len(s):
            return []

        p_dict = {}
        for letter in p:
            p_dict[letter] = 1 + p_dict.get(letter, 0)

        s_dict = {}
        first_frame = s[0:frame_size]
        for letter in first_frame:
            s_dict[letter] = 1 + s_dict.get(letter, 0)

        res = []
        if self.checkEq(s_dict, p_dict):
            res.append(0)

        for i in range(1, len(s) - frame_size+1):
            old_char = s[i-1]
            s_dict[old_char] -= 1

            new_char = s[i+frame_size-1]
            s_dict[new_char] = 1 + s_dict.get(new_char, 0)

            if self.checkEq(s_dict, p_dict):
                res.append(i)
        return res
