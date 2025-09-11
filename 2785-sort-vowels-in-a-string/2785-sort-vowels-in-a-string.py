class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        vs = []
        for c in s:
            if c in vowels:
                vs.append(c)
        
        vs.sort()
        vs = deque(vs)
        s = list(s)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vs.popleft()

        return "".join(s)