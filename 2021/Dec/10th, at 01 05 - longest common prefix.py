class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        i = 0
        is_done = False
        try:
            while not is_done:
                current_prefix = strs[0][i]
                for word in strs:
                    if word[i] != current_prefix:
                        is_done = True
                        break
                if not is_done:
                    prefix.append(current_prefix)
                i += 1
        except IndexError:
            pass
        return ''.join(prefix)