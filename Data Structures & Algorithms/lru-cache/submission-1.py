class Node:
    def __init__(self, key, val):
        self.key, self.val = key,val
        # pointer for previous node and next node
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        # left is Least recently used and right is most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        # doubly linked list connected
        self.left.next, self.right.prev = self.right, self.left
    
    # remove node from list 
    def remove(self, node):
        # we are removing the middle node and move the first node pointer to last and last node pointer to prev
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node in the middle
    def insert(self, node):
        # is self.right.prev, self.left? 
        prev, nxt = self.right.prev, self.right
        # since the current node is in the middle
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # todo: update to most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update key to new value
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
