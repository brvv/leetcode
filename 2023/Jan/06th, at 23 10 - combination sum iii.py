class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        curr = []

        def combinationSumRec(nums_left, current_sum, curr_num=1):
            if nums_left == 0 and current_sum == 0:
                ans.append(curr.copy())
                return
            elif nums_left <= 0 or current_sum <= 0:
                return
            elif curr_num > 9:
                return

            curr.append(curr_num)
            pick_curr = combinationSumRec(nums_left - 1, current_sum - curr_num, curr_num + 1)
            curr.pop()
            skip_curr = combinationSumRec(nums_left, current_sum, curr_num + 1)

        combinationSumRec(k, n)
        return ans 