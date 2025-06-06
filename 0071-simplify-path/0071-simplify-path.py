class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        cur = ""
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stk:
                        stk.pop()
                elif cur != "" and cur != ".":
                    stk.append(cur)
                cur = ''
            else:
                cur +=  c
        return "/" + "/".join(stk)

