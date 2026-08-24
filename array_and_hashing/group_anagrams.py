from typing import List

# Solution: 1 -------- Counting sort -------------


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        n = len(strs)

        for i in range(n):
            counter = {chr(i + 96): 0 for i in range(1, 27)}
            m = len(strs[i])

            for j in range(m):
                counter[strs[i][j]] += 1

            sorted_word = "".join(char * freq for char,
                                  freq in counter.items() if freq > 0)

            # check and put in anagrams hashmap
            if anagrams.get(sorted_word) is None:
                anagrams[sorted_word] = []
                anagrams[sorted_word].append(strs[i])
            else:
                anagrams[sorted_word].append(strs[i])

        return list(anagrams.values())

# Time: O(n * 27 * m)
# Space: O(k)

# Solution: 2 ----------------------- Bucket sort --------------------------


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        n = len(strs)

        for i in range(n):
            buckets = {chr(i + 96): [] for i in range(1, 27)}
            m = len(strs[i])

            for j in range(m):
                buckets[strs[i][j]].append(strs[i][j])

            print(buckets)
            sorted_word = ""
            
            for bucket in buckets.values():
                if len(bucket) > 0:
                    for char in bucket:
                        sorted_word += char

            # check and put in anagrams hashmap
            if anagrams.get(sorted_word) is None:
                anagrams[sorted_word] = []
                anagrams[sorted_word].append(strs[i])
            else:
                anagrams[sorted_word].append(strs[i])

        return list(anagrams.values())


# Time: O(n * 27 * m)
# Space: O(k)


obj = Solution2()
print(obj.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
