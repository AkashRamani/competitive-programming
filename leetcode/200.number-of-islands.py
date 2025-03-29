#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            Time: 
               O(N*M) -- Overall we simply traverse all the nodes
            Space: O(N*M) --> But can be made const if we modify the input grid smartly
        '''

        mask = [[0 for _ in row] for row in grid]

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == '1' and mask[i][j] == 0:
                mask[i][j] = 1
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i,j-1)
            return
        no_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and mask[i][j] == 0:
                    dfs(i, j)
                    no_of_islands+=1
    
        return no_of_islands
# @lc code=end

