class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stk = []

        for i, n in enumerate(arr):
            while stk and n < stk[-1][1]:
                j,m = stk.pop()
                left = j - stk[-1][0] if stk else j + 1
                right = i - j
                res = (res + m * left * right) % MOD
            stk.append((i,n))
        for i in range(len(stk)):
            j, n = stk[i]
            left = j - stk[i-1][0] if i > 0 else j + 1
            right = len(arr) - j
            res = (res + n * left * right) % MOD

        return res
