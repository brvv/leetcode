class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitXorSum = 0
        
        for num in nums:
            bitXorSum = bitXorSum ^ num
        return bitXorSum