class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        totalsum = 0
        for i in range(0,len(mat)):
            totalsum += mat[len(mat)-1-i][i]
        for i in range(len(mat)-1,-1,-1):
            totalsum += mat[i][i]
        if len(mat) % 2 != 0:
            midpoint = len(mat)//2
            totalsum -= mat[midpoint][midpoint]
        return totalsum