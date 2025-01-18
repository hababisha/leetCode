class Solution:
    def scoreOfString(self, s: str) -> int:
        l,r = 0, 1
        dmr = 0

        for _ in range(len(s) - 1):
            dmr += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r += 1
        return dmr



            


        