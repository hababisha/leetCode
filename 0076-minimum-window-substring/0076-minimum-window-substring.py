class Solution:
    def minWindow(self, s, t):
        target = Counter(t)

        def includes(window, target):
            for k,v in target.items():
                if window.get(k,0) < v:
                    return False
            return True
        
        window = defaultdict(int)
        l = 0
        min_len = float("inf")
        ans = ""

        for r in range(len(s)):
            window[s[r]] += 1

            while includes(window, target):
                if r-l+1 < min_len:
                    min_len = r-l+1
                    ans = s[l:r+1]

                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        return ans

sol = Solution()
s, t = "ADOBECODEBANC", "ABC"
print(sol.minWindow(s,t))
