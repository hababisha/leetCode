class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        n = len(questions)

        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            p, b = questions[i]
            take = p + dp(i + b + 1)
            skip = dp(i + 1)

            memo[i] = max(take, skip)
            return memo[i]

        return dp(0)
