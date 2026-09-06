from typing import List 

# Soltuion: 1 --------------- Sorting (Counting Sort) -------------

class Solution:
    def removeDuplicates(self, nums: List[int]) -> None:
        i, n = 0, len(nums)
        seen = set()
        
        while i < n:
            if nums[i] in seen:
                del nums[i]
                n -= 1
                continue
            seen.add(nums[i])
            i += 1
            
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        self.removeDuplicates(nums)
        
        # sort array
        counter = {i: 0 for i in range(min(nums), max(nums) + 1)}
        
        for num in nums:
            if counter.get(num) is None:
                counter[num] = 1
            else:
                counter[num] += 1
        
        i, n = 0, len(nums)
        
        for num, freq in counter.items():
            if freq > 0:
                j, m = 0, freq
                
                while i < n and j < m:
                    nums[i] = num
                    i += 1
                    j += 1

        # check
        lcs = set()
        prev_num = nums[0]
        count = 1
        i = 1
        
        while i < n:
            dis = nums[i] - prev_num
            
            if dis == 1:
                count += 1
            else:
                lcs.add(count)
                count = 1
            
            prev_num = nums[i]
            i += 1
        
        lcs.add(count)
        return max(lcs)

# Time: O(k + n)
# Auxiliary Space : O(k)

# obj = Solution()
# print(obj.longestConsecutive([2,20,4,10,3,4,5]))

# Solution: 2 ---------------- Hashmap ----------------------

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> None:
        nums_seen = {}
        
        for num in nums:
            nums_seen[num] = False
        
        n = len(nums)
        lcs = set()
        count = 0
        
        for i in range(n):
            if nums_seen.get(nums[i]) is False:
                nums_seen[num] = True
                count += 1
                
                next_num = nums[i] + 1
                
                while next_num in nums_seen:
                    nums_seen[next_num] = True
                    next_num += 1
                    count += 1
                
                prev_num = nums[i] - 1
                
                while prev_num in nums_seen:
                    nums_seen[prev_num] = True
                    prev_num -= 1
                    count += 1
                
                lcs.add(count)
                count = 0
        
        
        return max(lcs)

# Time: O(n)
# Auxiliary Space: O(k)

obj = Solution2()
print(obj.longestConsecutive([2,20,4,10,3,4,5]))

