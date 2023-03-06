class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        options = '123456789'
        ans = []

        for num_size in range(2, len(options) + 1):
            for ptr1 in range(0, len(options) + 1 - num_size):
                
                
                num = int(options[ptr1 : ptr1 + num_size])
                if low <= num <= high:
                    ans.append(num)

                if num > high:
                    return ans
        return ans


