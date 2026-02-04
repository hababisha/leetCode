class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pref = [0] * (n+1)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        ans = []
        for i in range(len(words)):
            w = words[i]
            if w[0] in vowels and w[-1] in vowels:
                pref[i+1] = pref[i] + 1
            else: pref[i+1] = pref[i]

        for l, r in queries:
            ans.append(pref[r+1]-pref[l]) 
        return ans