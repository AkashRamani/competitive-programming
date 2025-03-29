class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        '''
            DFS.. but run an outer loop over all the node
            everytime you call dfs from there are # of disconnected components
        '''

        adj = {i:[] for i in range(n)}
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
            
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1
        return count
        
