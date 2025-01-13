class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for i in c:
            ans+= ((c[i] - 1) //2 )
        return len(s) - (ans*2)