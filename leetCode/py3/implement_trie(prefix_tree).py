# 208. Implement Trie (Prefix Tree)
# Medium

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true

# Note:

#     You may assume that all inputs are consist of lowercase letters a-z.
#     All inputs are guaranteed to be non-empty strings.

class Node:

    def __init__(self):
        self.children = {};
        self.is_terminal = False;

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str, root=None) -> None:
        """
        Inserts a word into the trie.
        """
        root = root or self.root
        letter = word[0]
        if not root.children.get(letter, False):
            root.children[letter] = Node()
        if len(word) == 1:
            root.children[letter].is_terminal = True
        else:
            self.insert(word[1:], root.children[letter])

    def search(self, word: str, root=None) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = root or self.root
        if word == '':
            return True if root.is_terminal else False
        letter = word[0]
        if root.children.get(letter, False):
            return self.search(word[1:], root.children[letter])
        else:
            return False

    def startsWith(self, prefix: str, root=None) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = root or self.root
        if prefix == '': return True
        letter = prefix[0]
        if root.children.get(letter, False):
            return self.startsWith(prefix[1:], root.children[letter])
        else:
            return False
