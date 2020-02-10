# Suffix Trie Construction

# Write a class for a suffix-trie-like data structure. 
# The class should have a "root" property set to be the root node of the trie. 
# The class should support creation from a string and the searching of strings. 
# The creation method (called populateSuffixTrieFrom()) will be called 
# when the class is instantiated and should populate the "root" property of the class. 
# Note that every string added to the trie should end with 
# the special "endSymbol" character: "*".

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insert(i, string)

    def insert(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


word = 'invisible'
# word = 'test'
trie = SuffixTrie(word)
# print(trie.root)

def test_case(word):
    for i in reversed(range(len(word))):
        substring = word[i:]
        print(f'substring: {substring}')
        print('\t',trie.contains(substring))

# test_case(word)
