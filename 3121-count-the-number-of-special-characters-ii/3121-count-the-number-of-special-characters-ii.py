class Solution:
    def numberOfSpecialChars(self, s: str) -> int:
        m = defaultdict(int)
        m2 = defaultdict(int)
        ans = 0

        for i in range(len(s)):
            if s[i].isupper() and s[i] not in m:
                m[s[i]] = i
            if s[i].islower():
                m2[s[i]] = i

            
        for c in m2.keys():
            if m2[c] < m[c.upper()]:
                ans += 1
        return ans