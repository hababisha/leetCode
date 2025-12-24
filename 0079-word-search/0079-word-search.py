class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        visit = set()
        def inbound(i,j):
            return 0 <= i < m and 0 <= j < n
        def bt(i,j,k):
            if k == len(word):
                return True
            if not inbound(i,j) or (i,j) in visit or board[i][j] != word[k]:
                return False

            visit.add((i,j))
            for dr, dc in dirs:
                nr,nc = dr + i, dc + j
                if bt(nr,nc,k+1):
                    return True
            visit.remove((i,j))

            return False
        for r in range(m):
            for c in range(n):
                if bt(r,c,0):
                    return True
                visit = set()
        return False