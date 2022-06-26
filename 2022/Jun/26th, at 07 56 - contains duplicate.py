class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for item in nums:
            if item not in dic.keys():
                dic[item] = 1
            else:
                return True
        return False
        