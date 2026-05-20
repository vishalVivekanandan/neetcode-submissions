class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # maintain a counter for number of prereqs for reach course
            # set it to 0 initially
        degree = [0]*numCourses
        
        adjList = [[] for i in range(numCourses)]
        
        for src, dst in prerequisites:
            degree[dst] += 1
            adjList[src].append(dst)
        
        q = deque()

        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        
        finish = 0
        while q:
            node = q.popleft()
            finish +=1
            for nei in adjList[node]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)
        return finish == numCourses
 
        # create adj list and populate it while populating counter list

        # create a q and add courses that have no prereqs to it

        # keep var count
        # while q is non-empty:
            # pop value off
            # increment count
            # for values in adj[node]
                # decrement the val in rereq count
                # if val is 0, add it to q
        # return count == numCourses



