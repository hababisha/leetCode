class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL = 0
        setS = set()
        for r in range(len(s)):
            while s[r] in setS:
                setS.discard(s[l])
                l += 1
            setS.add(s[r])
            maxL = max(maxL,r - l + 1)
        return maxL
