from typing import List 

# Solution: 1 ------- using division operator ----------
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        prod_without_zero = 1
        zeros = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                prod_without_zero *= nums[i]
            else:
                zeros += 1
            total_prod *= nums[i]
        
        for j in range(n):
            if nums[j] == 0:
                if zeros > 1:
                    nums[j] = 0
                else:
                    nums[j] = prod_without_zero
            
            else:
                if zeros >= 1:
                    nums[j] = 0
                else:
                    nums[j] = total_prod // nums[j]
        
        return nums

# Time: O(n)
# Auxiliary Space: O(1)

obj = Solution1()
print(obj.productExceptSelf([1,2,4,6]))
print(obj.productExceptSelf([-1,0,1,2,3]))