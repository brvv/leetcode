class Solution:
    def getOrder(self, s):
            current_letter = s[0]
            count = 1
            res = []

            for letter in s[1::]:
                if letter == current_letter:
                    count += 1
                else:
                    item = [current_letter, count]
                    res.append(item)

                    current_letter = letter
                    count = 1
            res.append([current_letter, count])

            return res
    

    def expressiveWords(self, s: str, words: List[str]) -> int:
        target_order = self.getOrder(s)
        res = 0
        word_orders = [self.getOrder(word) for word in words]


        for order in word_orders:
            if len(order) != len(target_order):
                continue

            for target, word in zip(target_order, order):
                is_same_letter = target[0] == word[0]
                is_stretchy_letter = (target[1] == word[1]) or (target[1] >= 3 and word[1] <= target[1])

                if (not is_same_letter or not is_stretchy_letter):
                    break
            else:
                res += 1
        return res