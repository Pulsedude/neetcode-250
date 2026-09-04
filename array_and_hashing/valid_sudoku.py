from typing import List 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        # rows validation
        for row in range(n):
            seen = set()
            
            for col in range(n):
                digit = board[row][col]
                
                if digit.isdigit():
                    if digit in seen:
                        return False
                    seen.add(digit)
        
        # cols validation
        for col in range(n):
            seen = set()
            
            for row in range(n):
                digit = board[row][col]
                
                if digit.isdigit():
                    if digit in seen:
                        return False
                    seen.add(digit)
        
        # 3 x 3 box validation
        for row in range(0, n, 3):
            for col in range(0, n, 3):
                seen = set()
                
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        digit = board[i][j]
                        
                        if digit.isdigit():
                            if digit in seen:
                                return False
                            seen.add(digit)
        
        return True
            

# Time: O(n^2)
# Auxiliary Space: O(1)

obj = Solution()
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(obj.isValidSudoku(board))