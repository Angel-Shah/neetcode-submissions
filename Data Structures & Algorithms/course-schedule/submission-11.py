class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            adj_list[crs].append(preq)

        path = set()

        def dfs(crs):
            if crs in path:
                return False
            if adj_list[crs] == []:
                return True
            path.add(crs)
            for preq in adj_list[crs]:
                if not dfs(preq):
                    return False
            path.remove(crs)
            adj_list[crs]=[]
            return True
            
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True