class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.count += 1

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(node, idx) -> int:
            total = node.count
            for ch, child in node.children.items():
                next_pos = s.find(ch, idx)
                if next_pos != -1:
                    total += dfs(child, next_pos + 1)
            return total

        return dfs(trie.root, 0)