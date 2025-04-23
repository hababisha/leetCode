class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        m = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in m:
                if stk and stk[-1] == m[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return True if not stk else False
