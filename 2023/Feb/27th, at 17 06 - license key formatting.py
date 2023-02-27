class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_s = s.replace('-', '')
        group = ''
        groups = []

        for i in range(len(new_s) -1, -1, -1):
            char = new_s[i]
            group += char.upper()
            if len(group) == k:
                groups.append(group[::-1])
                group = ''
        if len(group) > 0:

            groups.append(group[::-1])
        
        groups = groups[::-1]
        return '-'.join(groups)