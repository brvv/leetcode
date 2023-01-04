class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counts = {}
        max_word_len = 0

        for word in words:
            word_counts[word] = 1 + word_counts.get(word, 0)
        
        for word in words:
            if word[0] == word[1] and word_counts[word] % 2 == 1:
                max_word_len += 2
                word_counts[word] -= 1
                break

        for word in words:
            rword = word[::-1]

            if word_counts[word] > 0 and rword in word_counts and word_counts[rword] > 0:
                if word == rword:
                    if word_counts[word] <= 1:
                        continue

                max_word_len += 4
                word_counts[word] -= 1
                word_counts[rword] -= 1
        
        return max_word_len