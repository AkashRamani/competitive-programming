#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        '''
            Time : O(m*n) --> linear in size of input
            Space : O(m*n) --> linear in size of input
        '''
        

        #shortest path from all rotton oranges.. 
        #and keep track of the orange that is max dist away

        # what about a node that is unreachable..?
        #  1. We can change something in-place
        #  2. maintain a global visited-set ... instead of set.. maintaining a grid

        global_visited = [[-val for val in row] for row in grid]
        # set1.update(set2)

        max_depth = -1

        DIR = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(row, col):
            visited = {(row,col):0}
            global_visited[row][col] = 0

            frontier = [(row,col)]
            
            level = 1
            while frontier:
                next_frontier = []
                for (r, c) in frontier:
                    for (dr, dc) in DIR:
                        if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[r+dr]) and not (r+dr, c+dc) in visited and grid[r+dr][c+dc] == 1:

                            visited[(r+dr, c+dc)] = level
                            if global_visited[r+dr][c+dc]>-1:
                                global_visited[r+dr][c+dc] = min(global_visited[r+dr][c+dc], level)
                            else:
                                global_visited[r+dr][c+dc] = level
                            next_frontier.append((r+dr, c+dc))
                
                frontier = next_frontier
                level +=1
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    bfs(i, j)

        #check if there are ay negative values..
        min_tries = -1
        for i in range(len(global_visited)):
            for j in range(len(global_visited[i])):
                if global_visited[i][j] < 0:
                    return -1
                min_tries = max(min_tries, global_visited[i][j])

        return min_tries


class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #method 2: 
        # follow neetcode's solution
        # Approch.. imagine a pseudo node that connects all the rotten oranges, and get a count of fresh oranges..

        # in one iteration you can get the count and the list of rotten oragneds intiallay..
        #Now consider that list as the frontier and run BFS on that..
        # that way you will only mainitain a SINGLE level counter.. (which signifies the time elapsed)
        # And has lesser things to tract

        DIR = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(frontier, fresh_count):
            visited = set()

            level = 0 #start with zero since we will return level+1, coz of while
            while frontier and fresh_oranges > 0:
                next_frontier = []
                for (r, c) in frontier:
                    for (dr, dc) in DIR:
                        if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[r+dr]) and not (r+dr, c+dc) in visited and grid[r+dr][c+dc] == 1:
                            visited.add((r+dr, c+dc))

                            next_frontier.append((r+dr, c+dc))
                frontier = next_frontier
                level +=1
            

        fresh_count = 0
        frontier = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    frontier.append((i, j))
                if grid[i][j] == 1:
                    fresh_count+=1
                
        minutes = bfs(frontier, fresh_count)

        return minutes if fresh_count == 0 else -1

# @lc code=end

