from typing import List

# Solution: 1 -------- Brute Force (bubble sort) --------------
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            swap = False
            
            for j in range(n - 1 - i):       
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swap = True
            
                if not swap:
                    return nums
        
        return nums

# Time: O(n^2)
# Space: O(1)

# obj = Solution()
# print(obj.sortArray([10,9,1,1,1,2,3,1]))
# print(obj.sortArray([1,2,3,4,5,6,9]))
                
# Solution: 2 ------------------- Bucket Sort --------------------
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        buckets = {i: [] for i in range(min(nums), max(nums) + 1)}
        
        for num in nums:
            if buckets.get(num) is None:
                buckets[num] = []
                buckets[num].append(num)
            else:
                buckets[num].append(num)
        
        i, n = 0, len(nums)
        
        for bucket in buckets.values():
            if len(bucket) > 0:
                j, m = 0, len(bucket)
                
                while i < n and j < m:
                    nums[i] = bucket[j]
                    i += 1
                    j += 1
            
        return nums

# Time: O(k + n)
# Time: O(k)

obj = Solution2()
print(obj.sortArray([10,9,1,1,1,2,3,1]))
print(obj.sortArray([1,2,3,4,5,6,9]))
                
        