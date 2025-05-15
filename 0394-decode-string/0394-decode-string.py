class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        currNum = 0
        currStr = ""

        for c in s:
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif c == '[':
                numStack.append(currNum)
                strStack.append(currStr)
                currNum = 0
                currStr = ""
            elif c == ']':
                repeatTimes = numStack.pop()
                prevStr = strStack.pop()
                currStr = prevStr + currStr * repeatTimes
            else:
                currStr += c

        return currStr
