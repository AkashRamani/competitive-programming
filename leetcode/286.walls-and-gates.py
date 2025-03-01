
#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(row,col):
            level = {(row, col): 0}

            count = 1
            frontier = [(row, col),]
            while frontier:
                nextt = []
                for (row, col) in frontier:
                    for (i,j) in DIR:
                        if 0 <= row+i < len(rooms) and 0 <= col+j < len(rooms[row+i]) and rooms[row+i][col+j] >0:
                            if not (row+i,col+j) in level:
                                level[(row+i,col+j)] = count
                                rooms[row+i][col+j] = min(rooms[row+i][col+j], count)
                                nextt.append((row+i, col+j))
                frontier = nextt
                count+=1

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    bfs(i,j)
# @lc code=end