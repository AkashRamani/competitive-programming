#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
            After each step you have roughly 1 or less than one places to place queen..
            
            Roughly O(N!) ~ O(N^N)
        '''

        
        row_map =set()
        left_diag = set()
        right_diag = set()

        grid = [['.']*n for _ in range(n)]

        valid_solutions = []

        def backtrack(col):
            if col >= n:
                valid_board = ["".join(row) for row in grid]
                valid_solutions.append(valid_board)
                return
            
            for row in range(n):
                if (row in row_map) or (row-col) in left_diag or (row+col) in right_diag:
                    continue

                else:
                    grid[row][col] = 'Q'
                    row_map.add(row)
                    left_diag.add((row-col))
                    right_diag.add((row+col))
                        
                    backtrack(col+1)

                    grid[row][col] = '.'
                    row_map.remove(row)
                    left_diag.remove((row-col))
                    right_diag.remove((row+col))

        backtrack(0)

# @lc code=end

