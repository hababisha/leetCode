class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.']*n for j in range(n)]
        col = set()
        posD = set()
        negD = set()
        
        def bt(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posD or (r-c) in negD:
                    continue

                col.add(c)
                posD.add(r+c)
                negD.add(r-c)
                board[r][c] = "Q" 
                bt(r+1)

                col.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                board[r][c] = "."
        bt(0) 
        return ans