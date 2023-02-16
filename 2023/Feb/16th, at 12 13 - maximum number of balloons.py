class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = {}
        for letter in 'balloon':
            b[letter] = 0

        for letter in text:
            if letter in b:
                b[letter] += 1

        b['l'] = b['l'] // 2
        b['o'] = b['o'] // 2

        
        return min(b.values())