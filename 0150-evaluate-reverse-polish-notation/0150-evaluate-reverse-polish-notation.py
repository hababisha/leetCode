class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = ['+', '-', "*", "/"]


        for token in tokens:
            if token not in operators:
                stk.append(int(token))
            else:
                if token == "+":
                    stk.append(stk.pop() + stk.pop())
                elif token == "/":
                    x, y = stk.pop(), stk.pop()
                    stk.append(int(y/x))
                elif token == "*":
                    stk.append(stk.pop()*stk.pop())
                else:
                    x, y = stk.pop(), stk.pop()
                    stk.append(y-x)
        return stk[-1]
