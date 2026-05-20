class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # empty adj list
        adj = [[] for _ in range(n)]
        # build the adj list from the edges
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # list of visited nodes (false by default)
        visit = [False] * n

        # dfs for each node's neighbord
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]: # if its not visited, mark it as such and call dfs on it
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True # this is visited
                dfs(node) # visit all of its neighbors, if visited 
                # when you're done visiting all neighbors of node, increment res
                res += 1
            # if it's visited, its not part of a new graph, dont increment res
        
        return res # total components in graph