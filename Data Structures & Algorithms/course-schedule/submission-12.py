class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for crs,preq in prerequisites:
            adj_list[crs].append(preq)

        path = set()
        cycle_detected = False
        def dfs(crs):
            nonlocal cycle_detected
            if cycle_detected:
                return
            if crs in path:
                cycle_detected = True
                return
            path.add(crs)
        
            for preq in adj_list[crs]:
                dfs(preq)
            path.remove(crs)
            adj_list[crs] = []
            
        for n in range(numCourses):
            dfs(n)
        
        if cycle_detected:
            return False
        return True