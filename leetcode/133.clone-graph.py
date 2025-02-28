#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
            Time: 
                O(N+M)
            
            space: 
                hashMap takes O(N) time -- to track visited nodes
                Stack takes at max O(H) -- why? coz DFS. Height for worst case is O(N)

                if we use BFS:
                    Traversal space -- O(N), both for visited and BFS 

        '''

        visited = {}
        def dfs(node):
            if not node:
                return None

            if node.val in visited:
                return visited.get(node.val)

            new_node = Node(node.val) 
            visited[node.val] =  new_node

            for neighbor in node.neighbors:              
                neighbor_node = dfs(neighbor)
                if neighbor_node:
                    new_node.neighbors.append(neighbor_node)
            return new_node

        new_node = dfs(node)
        return new_node
        

        new_node = Node()
        dfs(node)
# @lc code=end

