class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map containing num for key and list for val
        preMap = {i: [] for i in range(numCourses)}
        
        #  map each course to its prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []: # this course has no prereqs
                return True

            visiting.add(crs) # we've visited this one

            for pre in preMap[crs]: # for each item in val's prereq list
                if not dfs(pre):
                    return False # we've visited this already - cycle
            visiting.remove(crs) # remove to avoid mistaken cycle
            preMap[crs] = [] # no prereqs for crs
            return True # done

        for c in range(numCourses): # for each class and its prereqs
            if not dfs(c):
                return False # cycle detected
        return True # we're done!


