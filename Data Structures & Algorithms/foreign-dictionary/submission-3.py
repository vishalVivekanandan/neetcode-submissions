class Solution:
    def foreignDictionary(self, words):
        # construct adj
        adj = {c: set() for w in words for c in w}

        # put stuff into adj
        for i in range(len(words)-1):
            # smaller words
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if w1[0:minLen] == w2[0:minLen] and len(w1) > len(w2):
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True

            for nei in adj[node]:
                if dfs(nei):
                    return True
            visited[node] = False
            res.append(node)
        
        for k in adj:
            if dfs(k):
                return ""
        
        res.reverse()
        return ("").join(res)

        

            
