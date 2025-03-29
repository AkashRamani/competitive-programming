class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
            Maitain an adj list (as: a->b and b->a)

            if # edges >n-1, it has to form a cycle
            pick any random node and run DFS, if you can traverse all nodes without cycle return True.
        '''

        if len(edges) > n - 1: return False

        adj = {}
        for i in range(n):
            adj[i] = []

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
        dfs(0)
        return len(visited) == n 
