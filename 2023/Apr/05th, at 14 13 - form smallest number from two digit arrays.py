class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        num = 10000000000
        
        for num1 in nums1:
            for num2 in nums2:
                comb = int(str(num1) + str(num2))
                num = min(num, comb)
                comb = int(str(num2) + str(num1))
                num = min(num, comb)
                if num1 == num2:
                    num = min(num, num1)
        return num