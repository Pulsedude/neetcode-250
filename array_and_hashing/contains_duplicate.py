from typing import List 

# Solution: 1 ------ Counting hashmap ---------

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        
        for num in nums:
            if counter.get(num) is None:
                counter[num] = 1
            else:
                counter[num] += 1
        
        for freq in counter.values():
            if freq > 1:
                return True
            
        return False

# Time: O(n + k) 
# Space: O(k)


# Solution: 2 -------- Hashset Lookup -------------
class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False

# Time: O(n)
# Space: O(n)

    
obj = Solution2()
print(obj.hasDuplicate([1, 2, 3, 4]))