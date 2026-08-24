from typing import List

# Solution: 1 -------- counter hashmap ------------
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        
        for num in nums:
            if counter.get(num) is None:
                counter[num]  = 1
            else:
                counter[num] += 1
        
        result = nums[0]
        
        for i in nums:
            if counter.get(i) > counter.get(result):
                result = i
        return result

# Time: O(n)
# Space: O(k)


# Solution: 2 ------------ boyer moore's voting algorithm
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        n = len(nums)
        
        for i in range(n):
            if count == 0:
                candidate = nums[i]
                count += 1
            
            if nums[i] != candidate:
                count -= 1
            
            else:
                count += 1
        
        return candidate

# Time: O(n)
# Space: O(1)

# SolutionL 3 ----------- Brute force --------------
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        
        for i in range(n):
            num_count = 0
            
            for j in range(i, n):
                if nums[j] == nums[i]:
                    num_count += 1
            
            if num_count > n // 2:
                result = nums[i]
        
        return result    

# Time: O(n^2)
# Space: O(1)

obj = Solution3()
print(obj.majorityElement([5,5,1,1,1,5,5]))    
print(obj.majorityElement([2,2,2]))    
