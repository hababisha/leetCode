class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(cols+1) for r in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for  c in range(cols):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1-1][col2]
        left= self.sumMat[row2][col1-1]
        topLeft = self.sumMat[row1-1][col1-1]

        return bottomRight - above - left+ topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)