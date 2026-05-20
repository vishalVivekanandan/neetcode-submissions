class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        # two nodes
        self.left, self.right = Node(0,0), Node(0,0)
        # connect two nodes
        self.left.right = self.right
        self.right.prev = self.left
        

    def remove(self, node):
        # remove any node in our list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        # insert any node in rightmost position
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node # insert at middle
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # update most recent by removing and inserting to rightmost
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # return the node    
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove least used val from cache (hashmap) (this is the left ptr val)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]





        
