class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        dict1 = set({})
        for num in nums1:
            dict1.add(num)

        dict2 = set({})
        for num in nums2:
            dict2.add(num)

        for num in nums1:
            if num in dict2:
                return num
        return -1