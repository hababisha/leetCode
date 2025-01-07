class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j:
                    ans.append(words[i])
        return list(set(ans))
            
        