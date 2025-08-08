class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[m][j] = True

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]

        return dp[0][0]
