class Solution:
    def isValidCoord(self, coord, heights):
        if (coord[0] >= 0 and coord[0] < len(heights) and coord[1] >= 0 and coord[1] < len(heights[0])):
            return True
        return False
    
    def getAdjacentCoords(self, coord, heights):
        adjacentCoords = []
        
        newCoords = [[coord[0]-1, coord[1]], [coord[0]+1, coord[1]], [coord[0], coord[1]-1], [coord[0], coord[1]+1]]
        
        for pair in newCoords:
            if (self.isValidCoord(pair, heights)):
                adjacentCoords.append(pair)
        return adjacentCoords
                
    
    def getUnvisitedVals(self, coord, heights, isVisited):
        adjacent = self.getAdjacentCoords(coord, heights)
        res = []
        
        for newCoords in adjacent:
            if (not isVisited[newCoords[0]][newCoords[1]]):
                res.append(newCoords)
        return res
        
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        isVisited = [[False for _ in row] for row in heights]
        
        pacificStack = [[0, col] for col in range(len(heights[0]))]
        pacificStack.extend([row, 0] for row in range(1, len(heights)))
        pacificRes = set()
        
        print(pacificStack)
        
        while pacificStack:
            coords = pacificStack.pop()
            pacificRes.add((coords[0], coords[1]))
            isVisited[coords[0]][coords[1]] = True
            adjacent  = self.getUnvisitedVals(coords, heights, isVisited)
            
            
            for val in adjacent:
                if(heights[val[0]][val[1]] >= heights[coords[0]][coords[1]]):
                    pacificStack.append(val)
                    
        isVisited = [[False for _ in row] for row in heights]
        atlanticStack = [[len(heights)-1, col] for col in range(len(heights[0]))]
        atlanticStack.extend([row, len(heights[0])-1] for row in range(0, len(heights) -1))
        atlanticRes = set()
        
        print(atlanticStack)
        
        while atlanticStack:
            coords = atlanticStack.pop()
            atlanticRes.add((coords[0], coords[1]))
            isVisited[coords[0]][coords[1]] = True
            adjacent  = self.getUnvisitedVals(coords, heights, isVisited)
            
            
            for val in adjacent:
                if(heights[val[0]][val[1]] >= heights[coords[0]][coords[1]]):
                    atlanticStack.append(val)     
    
        return pacificRes.intersection(atlanticRes)