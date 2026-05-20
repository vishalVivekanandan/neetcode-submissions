class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w} # map each char to a set
        # indegree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1] # get ith and i+1th words
            
            # if the prefix if each word is the same but word 1 is longer 
            # than word 2, this order is invalid
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return "" 

            # iterate through each char of words
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # find ONLY the first instance of 
                    # differing chars within words
                    adj[w1[j]].add(w2[j]) 
                    # we know the char in word 2 comes 
                    # after the char in word 1
                    break 
        
        visit = {}
        res = []
        
        def dfs(c):
            if c in visit:
                return visit[c] # this will return true which means we detected a loop
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False        
            res.append(c) # post-order dfs
        
        # we can start anywhere in the graph
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
            

            
