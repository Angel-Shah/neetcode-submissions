class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            graph[crs].append(pre)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            graph[course] = []

            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True