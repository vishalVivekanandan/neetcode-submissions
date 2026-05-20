class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n nodes from 1-n
        
        # times: list of edges (ui, vi, ti)
            # ui is the source node 
            # vi is the target node 
            # ti is the time it takes for a signal to travel from the source to the target node 
        
        # k: node we will start from    

        # min time it takes for all nodes to recieve the signal (sum of shortest path vals!)
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visited = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue

            visited.add(n1)
            t = w1
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visited) == n else -1

            


