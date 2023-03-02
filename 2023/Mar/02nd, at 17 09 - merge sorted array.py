class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        lnums1 = len(nums1) - n
        lnums2 = len(nums2)

        count1 = 0
        count2 = 0
        
        while count1 < lnums1 and count2 < lnums2:
            item2 = nums2[count2]
            item1 = nums1[count1]

            if item1 <= item2:
                temp.append(item1)
                count1 += 1
            else:
                temp.append(item2)
                count2 += 1
            
        #copy the remaining nums:
        while count1 < lnums1:
            temp.append(nums1[count1])
            count1 += 1
        
        while count2 < lnums2:
            temp.append(nums2[count2])
            count2 += 1
        
        #copy temp to nums1
        for i, val in enumerate(temp):
            nums1[i] = val
        
        return nums1