class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #DFS toposort with cycle detection

        graph = {n:[] for n in range(numCourses)}

        for crs,pre in prerequisites:
            graph[crs].append(pre)

        topo = []
        visited = set()
        path = set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True
            
            path.add(crs)
            for nei in graph[crs]:
                if not dfs(nei):
                    return False
            path.remove(crs)
            visited.add(crs)
            topo.append(crs)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return []
        return topo