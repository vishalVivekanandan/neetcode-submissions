class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        test = [[] for i in range(n)]
        for a,b in edges:
            test[a].append(b)
            test[b].append(a)
        
        visit = [False]*n

        def dfs(node):
            for nei in test[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res+=1
        return res
