class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        max_elem = nums[-1]
        max_count = -1

        for elem in nums:
            counter[elem] = 1 + counter.get(elem, 0)

            if counter[elem] > max_count:
                max_elem = elem
                max_count = counter[elem]

        return max_elem