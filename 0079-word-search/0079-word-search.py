from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, k, visited):
            if k == len(word):
                return True
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                (i, j) in visited or 
                board[i][j] != word[k]):
                return False

            visited.add((i, j))

            res = (
                dfs(i + 1, j, k + 1, visited) or
                dfs(i - 1, j, k + 1, visited) or
                dfs(i, j + 1, k + 1, visited) or
                dfs(i, j - 1, k + 1, visited)
            )

            visited.remove((i, j))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0, set()):
                    return True
        return False
