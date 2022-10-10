class Solution:
    def is_palindrome(self, word):
        l = 0
        r = len(word) - 1
        while l < r:
            if word[l] != word[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(word, part=[], part_start=0):
            if part_start >= len(word):
                res.append(part)
                return
            for i in range(part_start + 1, len(word)+1):
                partition = word[part_start : i]
                if self.is_palindrome(partition):
                    dfs(word, part + [partition], i)
        dfs(s)
        return res