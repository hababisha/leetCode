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
        def dfs(j, root):
            if not root:
                return False
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children:
                        if child and dfs(i + 1, child): 
                            return True
                    return False
                else:
                    idx = ord(c) - ord('a')
                    if not cur.children[idx]:
                        return False
                    cur = cur.children[idx]
            return cur.is_end

        return dfs(0, self.root)
