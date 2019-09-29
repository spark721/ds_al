
# LeetCode
# 146
# Medium

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4



class LRUCache:

    def __init__(self, capacity: int):
    	'''
    	init empty head and empty tail dict
    	point the head and tail to each other
    	init empty cache dict
    	'''
    	self.capacity = capacity
    	self.head = {}
    	self.tail = {}
    	self.head['next'] = self.tail
    	self.tail['prev'] = self.head
    	self.cache = {}
        

    def get(self, key: int) -> int:
    	'''
    	if key is not in the cache, return -1
	    re-position the key's prev's next and the next's prev pointer to disconnect
	    re-position the key's prev and the key's next to attach before tail
		re-position the tail's prev's next and the tail's prev pointer to attach the key
		return the key's value
    	'''
    	if key not in self.cache: return -1

    	node = self.cache.get(key)

    	# disconnect the node from the chain
    	node['prev']['next'] = node['next']
    	node['next']['prev'] = node['prev']

    	# attach the node before the tail
    	node['next'] = self.tail
    	node['prev'] = self.tail['prev']

    	# re-assign the pointers on the tail side
    	self.tail['prev']['next'] = node
    	self.tail['prev'] = node

    	return node['val']
        

    def put(self, key: int, val: int) -> None:
    	'''
    	if get(key) is not -1, update the tail.prev's value
    	else
    	if capacity == cache's size
    	delete the node from cache
    	disconnect the node from the list
    	else
		create a new node and attach to the tail side
    	'''
    	if self.get(key) != -1:
    		self.tail['prev']['val'] = val
    	else:
    		if self.capacity == len(self.cache):
    			node = self.head['next']
    			del self.cache[node['key']]
    			self.head['next'] = node['next']
    			node['next']['prev'] = self.head

    		new_node = { 'key': key, 'val': val }
    		new_node['prev'] = self.tail['prev']
    		new_node['next'] = self.tail

    		new_node['prev']['next'] = new_node
    		self.tail['prev'] = new_node

    		self.cache[key] = new_node     


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)















