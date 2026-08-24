# Solution: 1 --------- sorting -------------
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time: O(n log n)
# Space: O(n)

# Solution: 2 -------- Counting hashmap --------


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {chr(i + 96): 0 for i in range(1, 27)}

        for i in s:
            counter[i] += 1

        sorted_s = "".join(char * freq for char,
                                   freq in counter.items() if freq > 0)
        
        # reset counter for string t
        counter = {chr(i + 96): 0 for i in range(1, 27)}
        
        for j in t:
            counter[j] += 1

        sorted_t = "".join(char * freq for char,
                           freq in counter.items() if freq > 0)

        return sorted_s == sorted_t

# Time: O(26 + n)
# Space: O(k + n)

obj = Solution2()
print(obj.isAnagram("racecar", "carrace"))
print(obj.isAnagram("jar", "jam"))
