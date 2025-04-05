#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        adj = {}
        parents = {}
        #since the graph froms a a cycle with jsut one extra node : #node = #edges 
        #And removing one cycle forming node node will remove the cycle
        for index, (i, j) in enumerate(edges):
            if not i in adj:
                adj[i] = []
            adj[i].append(j)

            if not j in adj:
                adj[j] = []
            adj[j].append(i)


        visited = set()
        visiting = set()

        cycle_edge = []
        def dfs(node, parent):
            if node in visiting:
                #cycle
                cycle_edge = [node, parent]
                return [node, parent]
            if node in visited:
                return 0
            
            visited.add(node)
            visiting.add(node)
            parents[node] = parent
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                cycle_edge = dfs(neighbor, node)
                if cycle_edge:
                    return cycle_edge
            visiting.remove(node)
            return 0

        # node, parent 
        cycle_edge= dfs(1, -1)
        parent, node = cycle_edge # draw the diagram and it iwll be clear why not node, parent

        cycle_nodes = set()
        cycle_nodes.add(parent) 
        
        while node != parent and node != -1:
            cycle_nodes.add(node)
            node = parents[node]

        # once we have the cycle nodes, we have to get to the latest node that forms the cycle and return it

        for index in range(len(edges) - 1, -1, -1):
            i, j = edges[index]

            if i in cycle_nodes and j in cycle_nodes:
                return [i, j]
        return [] #will never come here since all inputs have a cycle
        
# @lc code=end

