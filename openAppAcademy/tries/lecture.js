// lecture url
// https://open.appacademy.io/learn/full-stack-online/data-structures-and-algorithms/tries-lecture

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

    insert(word, root=this.root) {
        let letter = word[0];

        if (!(letter in root.children)) {
            root.children[letter] = new Node();
        }

        if (word.length === 1) {
            root.children[letter].isTerminal = true;
        } else {
            this.insert(word.slice(1), root.children[letter]);
        }
    }

    search(word, root=this.root) {
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
    }

    print(root=this.root) {
        for (let letter in root.children) {
            console.log(letter);
            this.print(root.children[letter]);
        }
    }
}

let myTrie = new Trie();
myTrie.insert('ten');
myTrie.insert('tea');
console.log(myTrie.search('ten'));   // true
console.log(myTrie.search('tea'));   // true
console.log(myTrie.search('te'));    // false
console.log(myTrie.search('tex'));   // false
