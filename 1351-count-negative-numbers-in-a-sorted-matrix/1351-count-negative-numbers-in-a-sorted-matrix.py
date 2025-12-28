class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        cols = len(grid[0])

        for row in grid:
            left, right = 0, cols - 1
            first_neg = cols 

            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    first_neg = mid
                    right = mid - 1
                else:
                    left = mid + 1

            count += cols - first_neg

        return count