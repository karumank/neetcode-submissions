class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}

        for course in range(numCourses):
            adjlist[course] = []
        
        for prereq in prerequisites:
            adjlist[prereq[0]].append(prereq[1])

        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if adjlist[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in adjlist[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            adjlist[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

            

        