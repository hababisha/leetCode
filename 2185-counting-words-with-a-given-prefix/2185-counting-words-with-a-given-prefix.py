class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self,word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def startswith(self, pref):
        cur = self.root
        for c in pref:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
            if cur .is_end:
                return True

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        t = Trie()
        t.add(pref)
        ans = 0
        for w in words:
            if t.startswith(w):
                ans += 1
        return ans