class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rows, cols = len(accounts), len(accounts[0])
        w = 0
        cw = 0
        for r in range(rows):
            for c in range(cols):
                cw += accounts[r][c]
            w = max(w, cw)
            cw = 0
        return w