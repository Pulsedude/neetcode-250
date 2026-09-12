class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, n, m = 0, 0, len(word1), len(word2)
        result = []

        while i < n and j < m:
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        
        if i < n:
            result.extend(word1[i:])
        
        if j < m:
            result.extend(word2[j:])
        
        return "".join(result)

# Time: O(n + m)
# Space: O(n + m)

obj = Solution()
print(obj.mergeAlternately("ab", "abbxxc"))