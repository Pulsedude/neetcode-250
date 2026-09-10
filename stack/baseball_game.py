from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        pointer = -1

        for op in operations:
            m = len(scores)
            
            if op[-1].isdigit():
                scores.append(int(op))
                pointer += 1
            
            elif op == "+":
                if m >= 2:
                    scores.append(scores[pointer] + scores[pointer - 1])
                    pointer += 1
            
            elif op == "C":
                if m >= 1:
                    scores.remove(scores[pointer])
                    pointer -= 1
            
            else:
                if m >= 1:
                    scores.append(2 * scores[pointer])
                    pointer += 1

        return sum(scores)

# Time: O(n)
# Auxiliary Space: O(m)

obj = Solution()
print(obj.calPoints(["5","-2","4","C","D","9","+","+"]))