class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None for i in range(n)] for j in range(n)]

        curr = 1

        top = 0
        bot = n - 1

        left = 0
        right = n - 1

        while top <= bot and left <= right:
            #left to right on top
            for i in range(left, right + 1):
                matrix[top][i] = curr
                curr += 1
            top += 1

            #top to bot, right side
            for i in range(top, bot+1):
                matrix[i][right] = curr
                curr += 1
            right -= 1


            #right to left on bot
            if  top <= bot and left <= right:
                for i in range(right, left - 1, -1):
                    matrix[bot][i] = curr
                    curr += 1
                    
                bot -= 1


            #bot to top, left side
            if  top <= bot and left <= right:
                for i in range(bot, top - 1, -1):
                    matrix[i][left] = curr
                    curr += 1
                
                left += 1

        return matrix