class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # initial prereqs for each course is empty list
        prereq = {c: [] for c in range(numCourses)}

        # fill it in
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # store sequential order of taking lists
        output = []
        visit, cycle = set(), set()

        # a course is either visited
        # or a course is bieng visited
        # or a course is unvisited

        def dfs(crs):
            if crs in cycle:
                return False # we detected a cycle
            if crs in visit:
                return True # we dont need to visit one twice

            # add to cycle (for future cycle detection)
            cycle.add(crs)  
            
            # go through every prereq of this course
            for pre in prereq[crs]:
                # if dfs of rereq evals to false, we've detected a cycle
                if dfs(pre) == False:
                    return False
            # we've visited all courses in this path so
                # remove crs from cycle
                # add crs to visited
                # and add it to output
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            
            # return true since we're allowed to take crs
            return True
        
        # run dfs for each course
        for c in range(numCourses):
            if dfs(c) == False: # cycle detected
                return []
        # otherwise we return output
        return output



