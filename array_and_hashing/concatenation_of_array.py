from typing import List

# solution: 1 ----------------------------------
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

# Time: O(n)
# Space: O(1)

# solution: 2 ---- iteration / simulation -------
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums.copy()
        n = len(nums)
        
        for i in range(n):
            result.append(nums[i])
        
        return result
    
# Time: O(n)
# Space: O(n)

obj = Solution2()
print(obj.getConcatenation([1,4,1,2]))
