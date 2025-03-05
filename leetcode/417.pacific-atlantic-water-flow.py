#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        '''
            Time and Space: O(m*n) : linear in size of input graph

            pacific nodes are nodes that touch pacific ocean, lly atlantic nodes

            We start with those nodes as our frontier and try climbing up the nodes, get all nodes that can be visited by pacific ocean while climbing

            'lly for atlantic

            and intersection of the two is the answer 
        '''
        
        DIR = [(0,1), (0,-1), (1, 0), (-1,0)]
        pacific_nodes = [(row, 0) for row in range(len(heights))] + [(0, col) for col in range(1, len(heights[0]))]

        atlantic_nodes = [(row, len(heights[0])-1) for row in range(len(heights))] + [(len(heights)-1,col) for col in range(0, len(heights[0])-1)]

        def bfs(frontier):
            visited = set(frontier)

            level = 0
            while frontier:
                new_frontier = []
                for (r,c) in frontier:
                    for (dr, dc) in DIR:

                        if 0<=(r+dr)<len(heights) and 0<=(c+dc)<len(heights[r]) and not (r+dr, c+dc) in visited and heights[r][c] <= heights[r+dr][c+dc]:
                            visited.add((r+dr, c+dc))
                            new_frontier.append((r+dr, c+dc))
                frontier = new_frontier
                level+=1
            return visited
                            
        visited_from_pacific =  bfs(pacific_nodes)
        visited_form_atlantic = bfs(atlantic_nodes)

        print('p nodes', pacific_nodes)
        print('a nodes', atlantic_nodes)

        print('vis from pac',visited_from_pacific )
        print('vis from atl', visited_form_atlantic)

        return list(visited_from_pacific.intersection(visited_form_atlantic))
      
# @lc code=end

