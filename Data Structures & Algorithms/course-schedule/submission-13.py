class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p_reqs = {i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            p_reqs[crs].append(preq)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if p_reqs[node] == []:
                return True
            visited.add(node)
            for preq in p_reqs[node]:
                if not dfs(preq):
                    return False
            visited.remove(node)
            p_reqs[node] = []
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True