class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:  
            return 0                               
        dp = {}                                   
        current_len = 1                            
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                current_len += 1                 
            else:
                current_len = 1               
            dp[s[i]] = max(dp.get(s[i], 0), current_len)

        return sum(dp.values()) 
