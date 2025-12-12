class Solution:
    def rle(self,s):
        s += '!'
        res = []
        p, c = s[0], 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                c += 1
                continue
            res.append(str(c)+p)
            p, c = s[i], 1
        return ''.join(res)
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        return self.rle(self.countAndSay(n-1))
 