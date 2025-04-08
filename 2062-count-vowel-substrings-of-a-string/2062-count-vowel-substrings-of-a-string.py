class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = {"a", "e", "i", "o", "u"}
        return sum(set(word[i:j]) == vowels for i in range(len(word)) for j in range(i + 1, len(word) + 1))