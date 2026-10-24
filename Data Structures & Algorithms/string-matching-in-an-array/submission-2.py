class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_suffixes(self, word: str) -> None:
        for i in range(len(word)):
            node = self.root
            for j in range(i, len(word)):
                idx = ord(word[j]) - ord('a')
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
                node.count += 1
    
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            node = node.children[idx]
        return node.count > 1

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        trie = Trie()
        for word in words:
            trie.insert_suffixes(word)
        
        for word in words:
            if trie.search(word):
                res.append(word)
        
        return res