class Node:
    def __init__(self,key:int,val:int):
        self.key,self.val = key,val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def insert(self, node):
        #insert at MRU
        prev,nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def remove(self,node):
        prev,nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        # del self.cache[node.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
     
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #evict the LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
