class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        res, val = 0,0
        for c in s:
            if c == "(":
                stk.append(0)
            else:
                mul = stk.pop()
                if mul == 0:
                    val = 1
                else:
                    val = mul * 2
                if not stk:
                    res += val
                else:
                    stk[-1] += val
        return res
