class Solution:
    def getBoxNumber(self, coord):
        row = coord[0]
        col = coord[1]
        box = (row // 3) * 3 + col // 3
        return box
    
    def findNextCoord(self, prevCoord):
        nextCoord = prevCoord.copy()
        if prevCoord[1] == 8:
            nextCoord[0] += 1
            nextCoord[1] = 0
        else:
            nextCoord[1] += 1
        return nextCoord
    
    def canInsert(self, value, coord, rows,columns, boxes):
        isInRow = value in rows[coord[0]]
        isInCol = value in columns[coord[1]]
        isInBox = value in boxes[self.getBoxNumber(coord)]
        return not isInRow and not isInCol and not isInBox
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set({}) for i in range(9)]
        columns = [set({}) for i in range(9)]
        boxes = [set({}) for i in range(9)]
        
        #fill the sets
        for row_i, row in enumerate(board):
            for col_i, item in enumerate(row):
                if not item == ".":
                    rows[row_i].add(item)
                    columns[col_i].add(item)
                    box_num = self.getBoxNumber([row_i, col_i])
                    boxes[box_num].add(item)
        
        def dfs(board, coord):
            if coord[0] == 9:
                return board
            
            if board[coord[0]][coord[1]] != ".":
                return dfs(board, self.findNextCoord(coord))
                
            
            for value in range(1, 10):
                val = str(value)
                
                if (self.canInsert(val, coord, rows, columns, boxes)):
                    board[coord[0]][coord[1]] = str(val)
                    rows[coord[0]].add(str(val))
                    columns[coord[1]].add(str(val))
                    boxes[self.getBoxNumber(coord)].add(str(val))
                
                    newBoard = dfs(board, self.findNextCoord(coord))
                    if newBoard:
                        return newBoard
                    
                    board[coord[0]][coord[1]] = "."
                    rows[coord[0]].remove(str(val))
                    columns[coord[1]].remove(str(val))
                    boxes[self.getBoxNumber(coord)].remove(str(val))
                    
            
            return False
        
        res = dfs(board, [0, 0])
        print(rows)
        return res
            
        
        