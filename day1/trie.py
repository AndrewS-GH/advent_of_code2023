from typing import Optional

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
    
    def get_first_word(self, phrase: str) -> Optional[str]:
        # returns first word or None
        node = self._root
        for i, char in enumerate(phrase):
            node = node.children.get(char)
            if not node:
                return None
            if node.is_end_of_word:
                return phrase[:i+1]
