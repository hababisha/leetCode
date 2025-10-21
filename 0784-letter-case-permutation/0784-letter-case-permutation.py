class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []
        def backtrack(i, cur):
            if i == len(s):
                self.res.append("".join(cur[::]))
                return

            if s[i].isdigit():
                cur.append(s[i])
                backtrack(i+1, cur)
            else:
                cur.append(s[i].lower())
                backtrack(i+1, cur)
                cur.pop()

                cur.append(s[i].upper())
                backtrack(i+1, cur)
            cur.pop()
        
        backtrack(0, [])
        return self.res