
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        dataVal = self.cache.get(key)
        del self.cache[key]
        self.cache[key] = dataVal
        return dataVal


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        
        
        self.cache[key] = value
 

        if len(self.cache) > self.capacity:
            lru = next(iter(self.cache))
            self.cache.pop(lru)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)