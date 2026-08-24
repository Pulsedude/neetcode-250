from typing import List

# Solution: --------- Bucket Sort -------------
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if counter.get(num) is None:
                counter[num] = 1
            else:
                counter[num] += 1
        
        buckets = {i: [] for i in range(min(list(counter.values())), max(list(counter.values())) + 1)}

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []
        k_count = 0

        for bucket in reversed(buckets.values()):
            if len(bucket) > 0:

                for num in bucket:
                    if k_count == k:
                        return result

                    result.append(num)
                    k_count += 1
        
        return result

# Time: O(n + k)
# Time: O(k)            

obj  = Solution()
print(obj.topKFrequent([1,2,2,3,3,3], 2))    