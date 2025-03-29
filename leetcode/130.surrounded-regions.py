#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        '''
            Time ~ O(2 m*n)= O(m*n)
            Space ~ O(m*n)

            From each O. 
            Explore all connected O's, if they thouch the border --make them return True. else False

            if they return False: they dont touch border and are surronded by Xs.
                So we need to fill all those nodes with X
                
        '''
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(row, col, visited):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
                return True
            if (row, col) in visited or board[row][col] == 'X': 
                return False
            
            visited.add((row, col))

            is_not_sorrounded = False
            for (dr, dc) in DIR:
                if dfs(row+dr, col+dc, visited):
                    is_not_sorrounded = True
            return is_not_sorrounded

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    visited = set()
                    if not dfs(row, col, visited):
                        for (i,j) in visited:
                            board[i][j] = 'X'
# @lc code=end

