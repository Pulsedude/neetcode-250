from typing import List

# Solution: 1 ------------- Array -------------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_s = "".join([i for i in reversed(s) if i.isalpha() or i.isalnum()]) # time: O(n), space: O(m) <- because spaces is removed
        filtered_s = "".join([i for i in s if i.isalpha() or i.isalnum()]) # time: O(n), space: O(m) <- because spaces is removed

        # current total time: O(n) and total max space in worst case: O(n) where n >= m , auxiliary space: O(m) -> which is extra space 
        i, j, m = 0, 0, len(filtered_s)

        while i < m: # loop gonna to take O(m) time so still current total time in wrost case will be: O(n) where n >= m
            s_chr = filtered_s[i].lower()
            rev_chr = reversed_s[j].lower()
            
            if s_chr != rev_chr:
                return False

            i += 1
            j += 1
        
        return True
        

# Time: O(n)
# Auxiliary Space: O(m)

# obj = Solution()
# print(obj.isPalindrome("Was it a car or a cat I saw?"))

# Solution: 2 ---------- Two Pointers ---------------
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            first, last = s[l], s[r]

            if not first.isalpha() and not first.isdigit():
                l += 1
                continue

            if not last.isalpha() and not last.isalnum():
                r -= 1
                continue
            
            else:
                if first.lower() != last.lower():
                    return False

                l += 1
                r -= 1

        return True

# Time: O(n)
# Auxiliary Space: O(1)

obj = Solution2()
print(obj.isPalindrome("Was it a car or a cat I saw?"))