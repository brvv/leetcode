class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False for i in arr]

        def canReachRec(curr_i):
            if curr_i >= len(arr) or curr_i < 0:
                return False

            if visited[curr_i]:
                return False
                
            curr_val = arr[curr_i]
            if curr_val == 0:
                return True

            left_i = curr_i - curr_val
            right_i = curr_i + curr_val
            visited[curr_i] = True
            left = canReachRec(left_i)
            right = canReachRec(right_i)
            visited[curr_i] = True

            return left or right
        return canReachRec(start)
