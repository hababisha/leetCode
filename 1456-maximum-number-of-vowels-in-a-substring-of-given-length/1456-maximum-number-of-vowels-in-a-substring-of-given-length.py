class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        res = 0
        for r in range(len(s)):
            count += 1 if s[r] in vowels else 0

            if r-l+1 > k:
                count -= 1 if s[l] in vowels else 0
                l += 1

            res = max(count, res)
        return res