#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

from typing import List

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Solution1 : For each value at i,j => comparing with 3 hash maps {each for row, col, block}

        '''defaultdict(set): doesnot give No key error, essentially comparable to doing.. in a dictionary
        hash_col = {for i in ra }
        for key, val in range(0, n):
            hash_col[key] = {}
            
        Linear Pass: Time Complexity O(n^2) // or Linear in the size of input
        Memory : O(n^2)
        '''
        n=len(board)

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(n):
            for col in range(n):
                element = board[row][col]
                if element == ".":
                    continue
                is_element_in_row = element in rows[row]
                is_element_in_col = element in cols[col]
                is_element_in_block = element in squares[(row//3, col//3)] #since tuple is immutable and can be used as a key
                if (is_element_in_row or is_element_in_col or is_element_in_block):
                    return False

                cols[col].add(element)
                rows[row].add(element)
                squares[(row//3, col//3)].add(element)
        return True
    
        '''Implement a solution that uses bit mask to do so, instead of hash maps'''

class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {key: set() for key in range(0,9)}
        cols = {key: set() for key in range(0,9)}
        blocks = {key: set() for key in range(0,9)}

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) in rows[i] or int(board[i][j]) in cols[j] or int(board[i][j]) in blocks[(i//3)*3 + j//3]:
                    return False
                
                rows[i].add(int(board[i][j]))
                cols[j].add(int(board[i][j]))
                blocks[(i//3)*3 + j//3].add(int(board[i][j]))
        return True       
    
sol = Solution2()
ans = sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)
print(f"function returned: {ans}")
# @lc code=end

