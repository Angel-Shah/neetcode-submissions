class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        visited = set()
        dag = {}
        for i in range(numCourses):
            dag[i] = []
        for c,pr in prerequisites:
            dag[c].append(pr)
        
        self.cycleDetected = False
        path = set()

        def dfs(node,result):
            if self.cycleDetected:
                return
            if node in path:
                self.cycleDetected = True
                return
            if node in visited:
                return
            # visited.add(node)
            path.add(node)
            # if dag[node] == []: # have reached end
            #     result.append(node)
            #     return result
            for neigh in dag[node]:
                dfs(neigh,result)
            result.append(node)
            path.remove(node)
            visited.add(node)


        for i in range(numCourses):
            dfs(i,result)

        if self.cycleDetected:
            return []
        else:
            return result
