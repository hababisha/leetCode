class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['[', '{', '(']
        hashMap = {'}' : '{', ']' : '[', ')' : '('}
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == hashMap[c]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
            
                    
        