class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans, sol = [], []
        def bt(pb): #bool to show if prev is zero or not
            if len(sol) == n:
                ans.append(''.join(sol))
                return
            
            sol.append('1')
            bt(False)
            sol.pop()
            
            if not pb:
                sol.append('0')
                bt(True)
                sol.pop()
        bt(False)
        return ans