from typing import List

# Solution: 1 --------- Array -----------
class Solution:
    def reverseString(self, s: List[str]) -> List[int]:
        elements = []
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            elements.append(s[i])
        
        for j in range(n):
            s[j] = elements[j]
        
        return s

# Time: O(n)
# Space: O(n)
# obj = Solution()
# print(obj.reverseString(["n","e","e","t"]))
        
            
# Solution: 2 -------- Two Pointers -----------
class Solution2:
    def reverseString(self, s: List[str]) -> List[int]:
        left, right = 0, len(s) - 1
        
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return s

# Time: O(n)
# Space: O(1)
obj = Solution2()
print(obj.reverseString(["n","e","e","t"]))
        
            
    