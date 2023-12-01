class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self, words: list[str] = None) -> None:
        self._root = Node()
        if words:
            for word in words:
                self.insert(word)
    
    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, phrase: str) -> tuple[bool, bool]:
        # returns (is_word, is_prefix)
        node = self._root
        for char in phrase:
            node = node.children.get(char)
            if not node:
                return False, False
    
        return node.is_end_of_word, bool(node.children)
