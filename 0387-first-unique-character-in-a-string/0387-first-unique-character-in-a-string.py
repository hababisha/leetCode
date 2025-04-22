class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = Counter(s)

        for i in range(len(s)):
            if mydict[s[i]] == 1:
                return i
        return -1