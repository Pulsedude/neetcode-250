from typing import List

# Solution: 1 ----------- Sorting (bubble sort) --------------
class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        return nums # for test case

# Time: O(n^2)
# Time: O(1)

# obj = Solution()
# print(obj.sortColors([1,0,1,2]))
            
# Solution: 2 ------------- Bucket sort (optimal sorting) ---------
class Solution2:
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = {i: [] for i in range(min(nums),  max(nums) + 1)}
        
        for num in nums:
            buckets[num].append(num)
        
        i, n = 0, len(nums)
        
        for bucket in buckets.values():
            if len(bucket) > 0:
                j, m = 0, len(bucket)
                
                while i < n and j < m:
                    nums[i] = bucket[j]
                    i += 1
                    j += 1
                    
        return nums # for test case
    

# Time: O(n)
# Space: O(1) # because array only contains elements 0, 1 and 2 max(2) <-

# obj = Solution2()
# print(obj.sortColors([1,0,1,2]))
            
    
# Solution: 3 --------------- DNF Algorithm (A sorting algorithm that is used to sort an array which contains at most 3 distinct elements) ---------------------
class Solution2:
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1
            
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        
        return nums
    
obj = Solution2()
print(obj.sortColors([2,2,1,1,0,2,1]))

