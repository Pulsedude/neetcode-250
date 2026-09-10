from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        
        while i < n:
            if nums[i] == val:
                del nums[i]
                n -= 1
                continue
            
            i += 1
        
        return len(nums)
    
# Time: O(n)
# Auxiliary Space: O(1)

obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))
                