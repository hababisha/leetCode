class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def backtrack(openn,closed):
            if len(sol) == 2 * n:
                ans.append(''.join(sol))
                return
            
            if openn < n:
                sol.append("(")
                backtrack(openn+1, closed)
                sol.pop()
            
            if openn > closed:
                sol.append(")")
                backtrack(openn, closed+1)
                sol.pop()
        backtrack(0,0)

        return ans