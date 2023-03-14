class Solution:
    def letterVal(self, letter):
        return ord(letter) - ord('a') + 1

    def stringSum(self, s, power):
        res = 0
        last_power = 1
        for i, letter in enumerate(s):
            res += self.letterVal(letter) * (last_power)
            last_power *= power
        return res
        

    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        first = s[0 : 0 + k]
        first_sum = self.stringSum(first, power)
        first_sum_modulo = first_sum % modulo
        max_power = (power ** (k - 1))

        if first_sum_modulo == hashValue:
            return first

        for i in range(1, len(s) - k + 1):
            #remove first element
            next_sum = first_sum - self.letterVal(s[i - 1])
            #decrease power of all power by 1
            next_sum = next_sum // power
            # add last element
            next_sum += (self.letterVal(s[i + k - 1]) * max_power)
            next_sum_modulo = next_sum % modulo

            if next_sum_modulo == hashValue:
                return s[i : i + k]
            first_sum = next_sum
        
