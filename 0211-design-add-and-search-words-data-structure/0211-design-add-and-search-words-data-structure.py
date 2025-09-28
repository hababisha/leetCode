class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()

            cur = cur.children[idx]
        cur.is_end = True


    def search(self, word: str) -> bool:
        return self.helper(0, word, self.root)
    
    def helper(self,i , word, cur):
        if i >= len(word):
            return cur.is_end
        res = False
        if word[i] == '.':
            for j in range(26):
                if cur.children[j] and self.helper(i + 1, word, cur.children[j]):
                    res = True
        else:
            j = ord(word[i]) - 97
            if cur.children[j] and self.helper(i + 1, word, cur.children[j]):
                res = True
        return res
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)