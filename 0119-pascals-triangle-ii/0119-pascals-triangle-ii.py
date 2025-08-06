class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = []

        for i in range(rowIndex+1):
            row = [1] * (i + 1) 
            for j in range(1, i):
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            pascal.append(row)

        return pascal[rowIndex]