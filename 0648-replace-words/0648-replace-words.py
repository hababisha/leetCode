class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            ind = ord(ch) - ord('a')
            if cur.children[ind] == None:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.is_end = True
    
    def replace(self, word:str):
        cur = self.root

        new = ""
        for ch in word:
            ind = ord(ch) - ord('a')
            if cur.children[ind] == None:
                return word
            cur = cur.children[ind]
            new += ch
            if cur.is_end:
                return new
        
        return word



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = WordDictionary()
        for each in dictionary:
            words.addWord(each)
        
        new_sentence = []
        for word in sentence.split():
            new_sentence.append(words.replace(word))
        
        return " ".join(new_sentence)