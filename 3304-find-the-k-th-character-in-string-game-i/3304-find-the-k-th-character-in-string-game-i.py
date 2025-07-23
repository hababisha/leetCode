class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        letters = 'abcdefghijklmnopqrstuvwxyz'
        def func(word):
            if len(word) >= k:
                return word[k-1]

            new_chars = ""
            for c in word:
                idx = letters.index(c)
                new_chars += letters[(idx + 1) % 26]
            
            word += new_chars
            return func(word)
        return func(word)