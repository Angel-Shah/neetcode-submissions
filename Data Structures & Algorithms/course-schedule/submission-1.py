# class GraphNode:
#     def __init__(self,val):
#         self.val = val
#         self.neighbours = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        graph = {}
        for pr in prerequisites:
            end,start = pr[0],pr[1]
            if start not in graph:
                graph[start] = []
            graph[start].append(end)
            if end not in graph:
                graph[end] = []

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for pr in graph[course]:
                if not dfs(pr):
                    return False
            visited.remove(course)
            graph[course] = []
            return True

        for c,pr in graph.items():
            if not dfs(c):
                return False
        return True