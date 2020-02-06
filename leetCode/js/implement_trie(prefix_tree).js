// 208. Implement Trie(Prefix Tree)
// Medium

// Implement a trie with insert, search, and startsWith methods.

//     Example:

// Trie trie = new Trie();

// trie.insert("apple");
// trie.search("apple");   // returns true
// trie.search("app");     // returns false
// trie.startsWith("app"); // returns true
// trie.insert("app");
// trie.search("app");     // returns true

// Note:

// You may assume that all inputs are consist of lowercase letters a - z.
// All inputs are guaranteed to be non - empty strings.

class Node {
    constructor() {
        this.children = {};
        this.isTerminal = false;
    }
}

class Trie {
    constructor() {
        this.root = new Node();
    }

    insert(word, root = this.root) {
        let letter = word[0];

        if (!(letter in root.children)) {
            root.children[letter] = new Node();
        }

        if (word.length === 1) {
            root.children[letter].isTerminal = true;
        } else {
            this.insert(word.slice(1), root.children[letter]);
        }
    };

    search(word, root = this.root) {
        let letter = word[0];
        if (word.length === 0) {
            if (root.isTerminal) {
                return true;
            } else {
                return false;
            }
        };

        if (letter in root.children) {
            return this.search(word.slice(1), root.children[letter]);
        } else {
            return false;
        }
    };

    startsWith(word, root = this.root) {
        let letter = word[0];
        if (word.length === 0) return true;

        if (letter in root.children) {
            return this.startsWith(word.slice(1), root.children[letter]);
        } else {
            return false;
        }
    };
};
