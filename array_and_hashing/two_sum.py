from typing import List

# Solution: 1 -------- brute force ----------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Time: O(n^2)
# Space: O(1)

# Solution: 2 ----------- Two Pass Hashmap -------------
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if (diff + num) == target:
                if diff in prevNums:
                    return [prevNums.get(diff), i]
            
            prevNums[num] = i
        
        return []

# Time: O(n)
# Space: O(k)

obj = Solution2()
print(obj.twoSum([3,4,5,6], 7))
print(obj.twoSum([4,5,6], 10))