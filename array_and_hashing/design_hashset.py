import numpy as np

# Solution: 1 ------------ using built-in dynamic array (python list)

class MyHashSet:

    def __init__(self):
        self.custom_set = []

    def add(self, key: int) -> None:
        self.custom_set.append(key)

    def remove(self, key: int) -> None:
        n = len(self.custom_set)

        for i in range(n - 1, -1, -1):
            if self.custom_set[i] == key:
                del self.custom_set[i]
                

    def contains(self, key: int) -> bool:
        for i in self.custom_set:
            if i == key:
                return True
        return False

# Time: O(n) -> if perform operations including contains or remove for only adding element (appending) -> O(1)
# Space: O(n)

# Solution: 2 ----------------- using static array with size 10^6

class MyHashSet2:
    
    def __init__(self):
        self.arr = np.array([False] * (10**6 + 2)) # size = O(10^6) (used numpy static array)
    
    def add(self, key: int) -> None:
        self.arr[key] = key   # O(1)
    
    def remove(self, key: int) -> None:
        self.arr[key] = False # O(1)
    
    def contains(self, key: int) -> bool:
        if self.arr[key] == False: # O(1)
            return False
        return True


# Time: O(1)
# Space: O(10^6) # too much space!

# obj = MyHashSet2()
# obj.add(2)
# obj.add(1)

# obj.remove(1)

# print(obj.contains(2))

# Solution: 3 --------------- Hashmap --------------

class MyHashSet3:
    
    def __init__(self):
        self.map = {} 
    
    def add(self, key: int) -> None:
        if self.map.get(key) is None: # O(1)
            self.map[key] = key
        else:
            self.map[key] = key
    
    def remove(self, key: int) -> None: # O(1)
        if self.map.get(key) is None:
            return None
        self.map[key] = False
    
    def contains(self, key: int) -> bool: # O(1)
        if self.map.get(key) is False or self.map.get(key) is None:
            return False
        
        return True


# Time: O(1)
# Space: O(n)

# obj = MyHashSet3()
# obj.add(2)
# obj.add(1)

# obj.remove(1)

# print(obj.contains(2))


# Solution: 4 ---------------- Map +  Dynamic array -------------------

class MyHashSet4:
    
    def __init__(self):
        self.map = {} 
    
    def hash(self, key: int) -> int:
        return key % 10
    
    def add(self, key: int) -> None:
        hash_val = self.hash(key)
        
        if self.map.get(hash_val) is None:
            self.map[hash_val] = []    
            self.map[hash_val].append(key)    
        
        else:
            keys = self.map.get(hash_val)
            n = len(keys)
            found = False

            for i in range(n):
                if keys[i] == key:
                    keys[i] = key
                    found = True
                    break
            
            if not found:
                self.map[hash_val].append(key)

                
    def remove(self, key: int) -> None: # O(1)
        hash_val = self.hash(key)
        
        if self.map.get(hash_val) is None:
            return None
        
        if len(self.map.get(hash_val)) <= 0:
            return None
        
        else:
            keys = self.map.get(hash_val)
            n = len(keys)

            for i in range(n):
                if keys[i] == key:
                    keys.remove(keys[i])
                    break
                    
                    
    def contains(self, key: int) -> bool: # O(1)
        hash_val = self.hash(key)
        
        if self.map.get(hash_val) is None:
            return False
                
        if len(self.map.get(hash_val)) <= 0:
            return False
                
        else:
            keys = self.map.get(hash_val)
                    
            for i in range(len(keys)):
                if keys[i] == key:
                    return True
                
        return False

# Time: O(n)
# Space: O(n)

obj = MyHashSet4()
obj.add(2)
obj.add(1)

obj.remove(1)

print(obj.contains(2))
