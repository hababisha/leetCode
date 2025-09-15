class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bl = set(brokenLetters)
        text = text.split()

        c = 0
        for w in text:
            for char in w:
                if char in brokenLetters:
                    c += 1
                    break
        return len(text) -c
