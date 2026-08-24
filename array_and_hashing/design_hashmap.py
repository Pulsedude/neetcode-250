# Solution: 1 ---------- Dynamic Array + Nested Dynamic Array or Tuple with size 2 ------------

class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        n = len(self.arr)
        found = False
        
        for i in range(n):
            if self.arr[i][0] == key:
                self.arr[i] = (key, value)
                found = True
                break
        
        if not found:
            self.arr.append((key, value))

    def get(self, key: int) -> int:
        for pair in self.arr:
            if pair[0] == key:
                return pair[1]
        return -1
        

    def remove(self, key: int) -> None:
        for pair in self.arr:
            if pair[0] == key:
                self.arr.remove(pair)
    

# Time: O(n)
# Space: O(n)

# obj = MyHashMap()
# obj.put(2, 1)
# obj.put(1, 1)
# obj.put(1, 2)
# obj.remove(2)
# print(obj.get(1))


# Solution: 2 --------------- built-in maps (not recommended) -----------------

class MyHashMap2:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if self.map.get(key) is None or self.map.get(key) is False:
            return -1
        
        return self.map.get(key)
        
    def remove(self, key: int) -> None:
        self.map[key] = False
        
# Time: O(1)
# Space: O(n)

# obj = MyHashMap2()
# obj.put(2, 1)
# obj.put(1, 1)
# obj.put(1, 2)
# obj.remove(2)
# print(obj.get(1))
# print(obj.get(2))


# Solution: 3 ------------- Fixed Size Static array ------------

class MyHashMap3:

    def __init__(self):
        self.arr = [False] * (10**6 + 2) # to much space!

    def put(self, key: int, value: int) -> None:
        self.arr[key] = [key, value]

    def get(self, key: int) -> int:
        if self.arr[key] == False:
            return -1
        
        return self.arr[key][1]
        

    def remove(self, key: int) -> None:
        self.arr[key] = False

# Time: O(1)
# Space: O(10^6)


# obj = MyHashMap3()
# obj.put(2, 1)
# obj.put(1, 1)
# obj.put(1, 2)
# obj.remove(2)
# print(obj.get(1))
# print(obj.get(2))


# Solution: 4 --------------- Map + Dynamic Array -----------------

class MyHashMap4:

    def __init__(self):
        self.map = {}
    
    def hash(self, key: int) -> int:
        return key % 10
    
    def put(self, key: int, value: int) -> None:
        hash_val = self.hash(key)
        
        if self.map.get(hash_val) is None:
            self.map[hash_val] = []
            self.map[hash_val].append((key, value))
        else:
            pairs = self.map.get(hash_val)
            found = False
            
            for i in range(len(pairs)):
                if pairs[i][0] == key:
                    pairs[i] = (key, value)
                    found = True
                    break
            
            if not found:
                self.map[hash_val].append((key, value))

    def get(self, key: int) -> int:
        hash_val = self.hash(key)

        if self.map.get(hash_val) is None:
            return -1
        
        if len(self.map.get(hash_val)) <= 0:
            return -1
        
        pairs = self.map.get(hash_val)
        for pair in pairs:
            if pair[0] == key:
                return pair[1]
        
        return -1

    def remove(self, key: int) -> None:
        hash_val = self.hash(key)
        
        if self.map.get(hash_val) is None:
            return None
                
        if len(self.map.get(hash_val)) <= 0:
            return None
        
        pairs = self.map.get(hash_val)
        for pair in pairs:
            if pair[0] == key:
                pairs.remove(pair)


# Time: O(n)
# Space: O(n)

obj = MyHashMap4()
obj.put(2, 1)
obj.put(1, 1)
obj.put(1, 2)
obj.remove(2)
print(obj.get(1))
print(obj.get(2))
print(obj.map)