class Solution:
    def countDigits(self, num):
        res = {}

        for digit in str(num):
            res[int(digit)] = 1 + res.get(int(digit), 0)
        return res
    
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = []

        i = 0

        while True:
            num = 2 ** i

            if num >= 10 ** 9:
                break

            powers.append(num)
            i += 1
        
        n_digits = self.countDigits(n)
        power_digits = [self.countDigits(num) for num in powers]

        for digits in power_digits:
            if n_digits == digits:
                return True
        return False
            
