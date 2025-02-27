#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            Time: O(m*n)
            Space: O(1)
        '''
        max_area =0

        def dfs(i, j):
            if (i<0 or i>=len(grid)) or (j<0 or j>=len(grid[0])) or (grid[i][j] !=1):
                return 0
            grid[i][j] = -1
            return 1+ dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] ==1:
                    max_area = max(max_area, dfs(row, col))
        return max_area

        '''
            This code takes a lot of time than code above, asymptotically they are same though
        '''

        # max_area =0

        # DIRECTIONS = [(0,1), (1,0), (0, -1), (-1, 0)] #r-d-l-up
        # def dfs(i, j):
        #     if (i<0 or i>=len(grid)) or (j<0 or j>=len(grid[0])):
        #         return 0

        #     if grid[i][j] ==1:
        #         grid[i][j] = -1
        #         cur_area =  1
        #         for (dx, dy) in DIRECTIONS:
        #             cur_area += dfs(i+dx, j+dy)
        #         return cur_area
        #     else:
        #         return 0
        
        # for row in range(len(grid)):
        #     for col in range(len(grid[row])):
        #         if grid[row][col] ==1:
        #             max_area = max(max_area, dfs(row, col))
        # return max_area

# @lc code=end

