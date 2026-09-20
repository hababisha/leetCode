class Solution:
    def reverseDegree(self, s: str) -> int:
        rev = 26
        ans = 0
        for index in range(len(s)):
            character = s[index]
            pos = index + 1
            
            rev = 26 -(ord(character)-ord("a"))
            ans += rev * pos

        return ans
