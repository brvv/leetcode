class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        stack = []
        val = 0
        ans = [[None for item in row] for row in mat]

        for row_i in range(len(mat)):
            for col_i in range(len(mat[row_i])):
                item = mat[row_i][col_i]
                if item == 0:
                    stack.append([row_i, col_i])

        while True: 
            new_stack = []

            while stack:
                row_i, col_i = stack.pop()
                if ans[row_i][col_i] is not None:
                    continue

                ans[row_i][col_i] = val

                top = [row_i - 1, col_i]
                bot = [row_i + 1, col_i]
                left = [row_i, col_i - 1]
                right = [row_i, col_i + 1]

                if top[0] >= 0 and ans[top[0]][top[1]] is None:
                    new_stack.append([top[0], top[1]])

                if bot[0] < len(ans) and ans[bot[0]][bot[1]] is None:
                    new_stack.append([bot[0], bot[1]])

                if left[1] >= 0 and ans[left[0]][left[1]] is None:
                    new_stack.append([left[0], left[1]])

                if right[1] < len(ans[0]) and ans[right[0]][right[1]] is None:
                    new_stack.append([right[0], right[1]])

            stack = new_stack.copy()
            val += 1


            if len(new_stack) == 0:
                break

        return ans




