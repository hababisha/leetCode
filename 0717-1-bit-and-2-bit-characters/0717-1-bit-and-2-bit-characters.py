class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1: return True
        stk = []
        for b in bits:
            while stk and b == 1 and stk[-1] == 0:
                stk.pop()
            if stk and stk[-1] == 1:
                stk.pop()
            else:
                stk.append(b)
        return len(set(stk)) != 0