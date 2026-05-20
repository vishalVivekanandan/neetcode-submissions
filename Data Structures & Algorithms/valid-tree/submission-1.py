class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if the edges are all connected and there are no cycles, return trie

        if len(edges) > (n-1):
            return False
        # this means there are nodes unconnected
        # in fully connected graph with n vertices, there are exactly n-1 edges

        adj = [[] for _ in range(n)]    #empty adj matrix

        # populate it
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set() #track visited nodes

        def dfs(node, par):
            if node in visit:
                return False # cycle exists

            visit.add(node) #we've visited it

            for nei in adj[node]: #iterate through all neighbors of node
                if nei == par:
                    continue # false positive for cycle, 
                    # we would go back and forth between two nodes 
                    # and assume a cycle if we didnt store prev node visited
                    # so we break out of this if this is the case
                
                if not dfs(nei, node): # we found a cycle
                    return False
            return True # we've visited all noted and there's not a cycle
        
        return dfs(0,-1) and len(visit) == n
        
        