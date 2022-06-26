class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        for item in nums:
            if item not in dic:
                dic.add(item)
            else:
                return True
        return False
        