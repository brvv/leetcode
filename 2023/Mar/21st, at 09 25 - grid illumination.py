class Solution:
    def getLines(self, coords):
        rowNum = coords[0]
        colNum = coords[1]
        diagIncNum = sum(coords)
        diagDecNum = coords[1] - coords[0]
        return [rowNum, colNum, diagIncNum, diagDecNum]
    
    def getAdjacentCoords(self, coords, n):
        rowMin = max(0, coords[0] - 1)
        rowMax = min(n, coords[0] + 2)
        colMin = max(0, coords[1] - 1)
        colMax = min(n, coords[1] + 2)

        ans = []
        for row_i in range(rowMin, rowMax):
            for col_i in range(colMin, colMax):
                ans.append([row_i, col_i])
        return ans

    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # for checking whether something is lit up
        # format : {row/col/diag num : number of lamps that light it}
        rows = defaultdict(int)
        cols = defaultdict(int)
        diagInc = defaultdict(int)
        diagDec = defaultdict(int)

        # for checking if something is a source in const time
        sources = set()

        # if we turn off something that is not a source, do not do anything

        for lamp in lamps:
            tlamp = tuple(lamp)
            [rowNum, colNum, diagIncNum, diagDecNum] = self.getLines(lamp)
            if tlamp not in sources:
                sources.add(tlamp)
                rows[rowNum] += 1
                cols[colNum] += 1
                diagInc[diagIncNum] += 1
                diagDec[diagDecNum] += 1


        res = []

        for query in queries:
            [rowNum, colNum, diagIncNum, diagDecNum] = self.getLines(query)
            # check if illuminated
            if ((rowNum in rows and rows[rowNum] > 0) or 
            (colNum in cols and cols[colNum] > 0) or 
            (diagIncNum in diagInc and diagInc[diagIncNum] > 0) or 
            (diagDecNum in diagDec and diagDec[diagDecNum] > 0)):
                res.append(1)
            else:
                res.append(0)

            for neighbour in self.getAdjacentCoords(query, n):
                [rowNum, colNum, diagIncNum, diagDecNum] = self.getLines(neighbour)
                tneighbour = tuple(neighbour)
                if tneighbour in sources:
                    sources.remove(tneighbour)
                    rows[rowNum] -= 1
                    cols[colNum] -= 1
                    diagInc[diagIncNum] -= 1
                    diagDec[diagDecNum] -= 1
        return res



            

            



