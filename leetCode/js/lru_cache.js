
// LeetCode
// # 146
// Medium


/*

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 * capacity * );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

*/

class LRUCache {
 	constructor(capacity) {
 		this.capacity = capacity;
 		this.head = {};
 		this.tail = {};
 		this.head.next = this.tail;
 		this.tail.prev = this.head;
 		// this.cache = {};
 		this.cache = new Map();
 	}
 
    get(key) {
        if (!this.cache.has(key)) return -1;

        let node = this.cache.get(key);

        // re-assign current node's prev and next
        node.prev.next = node.next;
        node.next.prev = node.prev;

        // attach the node right after the head
        node.prev = this.head;
        node.next = this.head.next;

        // re-assign head and head's next
        this.head.next.prev = node;
        this.head.next = node;


        return node.val;
    };

    put(key, val) {
        if (this.get(key) !== -1) {
            this.head.next.val = val;
        } else {
            if (this.cache.size === this.capacity) {
            	let node = this.tail.prev;
                // delete this.cache[node.key];
                this.cache.delete(node.key);
                this.tail.prev = this.tail.prev.prev;
                this.tail.prev.next = this.tail;
            }

            let newNode = { key, val, };

            newNode.prev = this.head;
            newNode.next = this.head.next;

            this.head.next.prev = newNode;
            this.head.next = newNode;

            this.cache.set(key, newNode);
        }
    };

}