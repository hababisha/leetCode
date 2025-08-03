class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        memo = {}
        def dp(i, j):
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1)- i
            
            key = (i, j)

            if (i, j) not in memo:
                if w1[i] == w2[j]:
                    memo[(i, j)] = dp(i+1, j+1)
                else:
                    ins = 1 + dp(i+1, j)
                    rep = 1 + dp(i+1, j+ 1)
                    dele = 1 + dp(i, j+1)

                    memo[(i, j)] = min(ins,rep,rep)
            
            return memo[(i, j)]
        
        return  dp(0,0)