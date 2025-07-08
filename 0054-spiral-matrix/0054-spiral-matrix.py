class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix or not matrix[0]:
            return ans
        
        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:

            for i in range(colBegin, colEnd + 1):
                ans.append(matrix[rowBegin][i])
            rowBegin += 1

            for j in range(rowBegin, rowEnd + 1):
                ans.append(matrix[j][colEnd])
            colEnd -= 1

            if rowBegin <= rowEnd:
                for k in range(colEnd, colBegin - 1, -1):
                    ans.append(matrix[rowEnd][k])
                rowEnd -= 1

            if colBegin <= colEnd:
                for l in range(rowEnd, rowBegin - 1, -1):
                    ans.append(matrix[l][colBegin])
                colBegin += 1

        return ans
