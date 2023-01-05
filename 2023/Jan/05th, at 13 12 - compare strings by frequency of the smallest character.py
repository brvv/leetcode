class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def freq_lsc(string):
            freqs = {}
            min_freq = 10000000000000
            ans_letter = -1

            for letter in string:
                lex = ord(letter)
                freqs[letter] = 1 + freqs.get(letter, 0)
                if lex <= min_freq:
                    min_freq = lex
                    ans_letter = letter
            return freqs[ans_letter]

        def binary_search(target, arr):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2
                mid_val = arr[mid]

                if mid_val < target:
                    low = mid + 1

                elif mid_val >= target:
                    high = mid - 1

            return low

        def insertion_point(target, arr):
            search = binary_search(target+1, arr)

            missing = len(arr) - search

            return missing


        queries_f = list(map(freq_lsc, queries))
        words_f = sorted(list(map(freq_lsc, words)))
        res = []

        print(queries_f)
        print(words_f)

        for query in queries_f:
            res.append(insertion_point(query, words_f))

        return res
