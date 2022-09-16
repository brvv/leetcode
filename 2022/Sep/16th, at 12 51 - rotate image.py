class Solution:
    def getNewCoords(self, oldCoords, size):
        oldRow = oldCoords[0]
        oldCol = oldCoords[1]
        
        numRows = size[0]
        numColumns = size[1]
        
        newRow = oldCol
        newCol = numRows - oldRow - 1
        
        return [newRow, newCol]
    
    
    def rotate(self, matrix: List[List[int]]) -> None:
        isModified = [[False for item in row] for row in matrix]
        
        size = [len(matrix), len(matrix[0])]
        
        for item_row, row in enumerate(matrix):
            for item_col, item  in enumerate(row):
                if isModified[item_row][item_col]:
                    continue
                    
                currentCoords = [item_row, item_col]                
                newCoords1 = self.getNewCoords(currentCoords, size)
                newCoords2 = self.getNewCoords(newCoords1, size)
                newCoords3 = self.getNewCoords(newCoords2, size)
                newCoords4 = currentCoords
                
                # one to two
                temp2 = matrix[newCoords1[0]][newCoords1[1]]
                matrix[newCoords1[0]][newCoords1[1]] = matrix[currentCoords[0]][currentCoords[1]]
                isModified[newCoords1[0]][newCoords1[1]] = True
                
                # two to three
                temp3 = matrix[newCoords2[0]][newCoords2[1]]
                matrix[newCoords2[0]][newCoords2[1]] = temp2
                isModified[newCoords2[0]][newCoords2[1]] = True
                
                # three to four
                temp4 = matrix[newCoords3[0]][newCoords3[1]]
                matrix[newCoords3[0]][newCoords3[1]] = temp3
                isModified[newCoords3[0]][newCoords3[1]] = True
                
                # four to one
                matrix[newCoords4[0]][newCoords4[1]] = temp4
                isModified[newCoords4[0]][newCoords4[1]] = True