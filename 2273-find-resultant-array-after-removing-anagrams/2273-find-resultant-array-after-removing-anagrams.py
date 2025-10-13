class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stk = [words[0]]
        for w in words[1:]:
            if Counter(stk[-1]) == Counter(w):
                continue
            stk.append(w)
        return stk