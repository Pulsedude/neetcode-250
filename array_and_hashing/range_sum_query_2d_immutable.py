from typing import List

# Solution: 1 --------------- Brute Force ---------------
class NumMatrix: 
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                result += self.matrix[i][j]
        
        return result

# Time: O(n^2)
# Auxiliary Space: O(1)


# obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
# print(obj.sumRegion(2,1,4,3))
# print(obj.sumRegion(1,1,2,2))
# print(obj.sumRegion(1,2,2,4))


# Solution: 2 ------------------------ Prefix Sum --------------------------
class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        for submat in range(len(self.matrix)):
            arr = self.matrix[submat]
            n = len(arr)
            
            for i in range(1, n):
                arr[i] = arr[i - 1] + arr[i]
        
                 
        for submat in range(1, len(self.matrix)):
            arr = self.matrix[submat]
            n = len(arr)
            upper_row = self.matrix[submat - 1]
            
            for i in range(n):
                arr[i] = arr[i] + upper_row[i]
                
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.matrix[row2][col2]
        
        if row1 < 0 and col1 < 0:
            return result
        
        if row1 < 0:
            result = result - self.matrix[row2][col1 - 1]
            return result
        
        if col2 < 0:
            result = result - self.matrix[row1 - 1][col2]
            return result
        
        result = result - self.matrix[row1 - 1][col2] - self.matrix[row2][col1 - 1] + self.matrix[row1 - 1][col1 - 1]
        return result


# Time: O(1)
# Auxiliary Space: O(1)

obj = NumMatrix2([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])

print(obj.sumRegion(2,1,4,3))

