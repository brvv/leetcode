class MyHashMap:

    def __init__(self):
        self.table = [None for i in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        while key >= len(self.table):
            self.table.append(None)
        
        self.table[key] = value
        

    def get(self, key: int) -> int:
        if key < len(self.table):
            return self.table[key] if self.table[key] is not None else -1
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key < len(self.table):
            self.table[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)