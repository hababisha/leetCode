class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an = int(a, 2)
        bn = int(b,2)
        return bin(an+bn)[2:]