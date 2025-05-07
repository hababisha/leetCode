class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(self, rows, targ):
            l=0
            r= len(rows) - 1

            while l <= r:
                mid = (l+r) // 2
                if rows[mid] == targ:
                    return True
                elif targ < rows[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        for r in matrix:
            if binarySearch(self, r, target):
                return True
        return False
