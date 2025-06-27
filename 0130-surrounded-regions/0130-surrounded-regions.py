class Solution(object):
    def solve(self, board):

        if not board: return
        row, col = len(board), len(board[0])
        q = collections.deque()
        
        for r in range(row):
            for c in range(col):
                if r in [0, row-1] or c in [0, col-1] and board[r][c]=='O':
                    q.append((r,c))
                    
        while q:
            x, y = q.popleft()
            if 0 <= x < row and 0 <= y < col and board[x][y] == 'O':
                board[x][y] = 'D'              
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:                
                    q.append((x+dx, y+dy))
                    
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'D':
                    board[r][c] = 'O'
        return board
