class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def getNewCoords(oldCoords, size):
            oldRow = oldCoords[0]
            oldCol = oldCoords[1]
            
            newRow = oldCol
            newCol = size[0] - oldRow - 1

            return [newRow, newCol]
        """
        Do not return anything, modify matrix in-place instead.
        """

        size = [len(matrix), len(matrix)]


        for row_i in range(0, len(matrix)//2 + len(matrix)%2):
            for col_i in range(row_i, len(matrix) - row_i - 1):
                currentCoords = [row_i, col_i]                
                newCoords1 = getNewCoords(currentCoords, size)
                newCoords2 = getNewCoords(newCoords1, size)
                newCoords3 = getNewCoords(newCoords2, size)
                newCoords4 = currentCoords
                
                # one to two
                temp2 = matrix[newCoords1[0]][newCoords1[1]]
                matrix[newCoords1[0]][newCoords1[1]] = matrix[currentCoords[0]][currentCoords[1]]
                
                # two to three
                temp3 = matrix[newCoords2[0]][newCoords2[1]]
                matrix[newCoords2[0]][newCoords2[1]] = temp2
                
                # three to four
                temp4 = matrix[newCoords3[0]][newCoords3[1]]
                matrix[newCoords3[0]][newCoords3[1]] = temp3
                
                # four to one
                matrix[newCoords4[0]][newCoords4[1]] = temp4

# side = len(mat[0])
# row col
# col side - row
# side - row side - col
# col row