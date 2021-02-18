class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if self.dict.get(key,None)==None:
            return -1
        val = self.dict.pop(key)
        self.dict[key] = val   
        return val        

    def put(self, key: int, value: int) -> None:
        if self.dict.get(key,None)!=None:    
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]         
        self.dict[key] = value