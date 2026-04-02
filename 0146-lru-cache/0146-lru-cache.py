class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    def deleteNode(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.next = node.prev = None
    
    def insertNode(self, node):
        prevNode, nextNode = self.mru.prev, self.mru
        
        prevNode.next, node.prev = node, prevNode
        node.next, nextNode.prev = nextNode, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.deleteNode(node)
        self.insertNode(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deleteNode(self.cache[key])

        node = Node(key,value)
        self.cache[key] = node
        self.insertNode(node)

        if len(self.cache) > self.capacity:
            del self.cache[self.lru.next.key]
            self.deleteNode(self.lru.next)





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)