class Solution:
    def reverseWords(self, s: str) -> str:
        newlist = s.split()
        empty=''

        for word in newlist:
            for j in range(len(word)-1, -1, -1):
                empty += word[j]
            empty += ' '
        
        return empty.strip()