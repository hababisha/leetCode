class Solution:
    def splitString(self, s: str) -> bool:
        curr = []

        def backtrack(indx):
            if indx >= len(s):
                return len(curr) >= 2

            for i in range(indx, len(s)):
                v = int(s[indx:i+1])
                if not curr or v == curr[-1] - 1:
                    curr.append(v)
                    if backtrack(i+1):
                        return True
                    curr.pop()

            return False

        return backtrack(0)