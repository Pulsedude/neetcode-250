from typing import List
from itertools import zip_longest


# Solution: 1 ---------- Horizontal Scanning --------------
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        
        for i in range(len(strs)):
            prefix_builder = ""
            prefix_of_i = []
            
            for j in range(len(strs[i]) - 1):
                prefix_builder += strs[i][j]
                prefix_of_i.append(prefix_builder)

            prefix.append(prefix_of_i)
        
        lcp = ""
        
        print(prefix)
        for word_prefix in zip_longest(*prefix, fillvalue=None):
            if all(i == word_prefix[0] for i in word_prefix):
                if len(lcp) < len(word_prefix[0]):
                    lcp = word_prefix[0]
                
        return lcp

# Time: O(n * m)
# Space: O(n * m)


# Solution: 2 --------------- Vertical Scanning -------------------
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        current_lcp = ""
        
        for i in range(1, len(strs)):
            lcp_builder = ""
            p1, p2 = 0, 0
            
            while (
                (p1 < len(first_word) and (p2 < len(strs[i]))) if i == 1 else
                (p1 < len(current_lcp)) and (p2 < len(strs[i]))
            ):
                if (
                    (first_word[p1] != strs[i][p2]) if i == 1 else
                    (current_lcp[p1] != strs[i][p2])
                ):
                    break
                
                lcp_builder += strs[i][p2]
                p1 += 1
                p2 += 1
            
            current_lcp = lcp_builder
        
        return current_lcp

# Time: O(n * min(l, strs[i]))
# Space: O(l)
        
obj = Solution2()
print(obj.longestCommonPrefix(["bat","bag","bank","band"]))
print(obj.longestCommonPrefix(["dance","dag","danger","damage"]))
print(obj.longestCommonPrefix([""]))