class Solution:
    def weirdDivision(self, nums, divisor):
        res = 0

        for num in nums:
            res += math.ceil(num / divisor)
        return res

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start=1
        arr_max = max(nums)
        end=arr_max

        smallestDivisor = 10000000

        
        while start <= end:
            divisor = (start + end) // 2
            divResult = self.weirdDivision(nums, divisor)
            if divResult <= threshold:
                smallestDivisor = min(smallestDivisor, divisor)
                end = divisor - 1
            elif divResult > threshold:
                start = divisor + 1
        return smallestDivisor
        return -1