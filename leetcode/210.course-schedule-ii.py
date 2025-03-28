#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        '''
            DFS is Order of # nodes + # edges
            Time: O(V+E)
            Space: O(V+E)
        '''
        
        
        adj = {i: [] for i in range(numCourses)} 
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        visited = set()
        visiting = set()
        order = []
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
                    
            
            visiting.remove(node)
            visited.add(node)
            
            order.append(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order[::-1]


# @lc code=end

