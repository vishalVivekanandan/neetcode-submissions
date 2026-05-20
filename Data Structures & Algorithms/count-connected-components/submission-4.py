class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i: [] for i in range(n)}
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()
        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        res = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                visit.add(node)
                res+=1
        return res

        # test = [[] for i in range(n)]
        # for a,b in edges:
        #     test[a].append(b)
        #     test[b].append(a)
        
        # visit = [False]*n

        # def dfs(node):
        #     for nei in test[node]:
        #         if not visit[nei]:
        #             visit[nei] = True
        #             dfs(nei)
        # res = 0
        # for node in range(n):
        #     if not visit[node]:
        #         visit[node] = True
        #         dfs(node)
        #         res+=1
        # return res
