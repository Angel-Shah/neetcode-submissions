# class GraphNode:
#     def __init__(self,val):
#         self.val = val
#         self.neighbours = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # result = []
        # visited = set()
        dag = {}
        for i in range(numCourses):
            dag[i] = []
        for c,pr in prerequisites:
            dag[c].append(pr)
        
        self.cycleDetected = False
        path = set()

        def dfs(node):
            if self.cycleDetected:
                return
            if node in path:
                self.cycleDetected = True
                return
            # if node in visited:
            #     return
                
            path.add(node)
            
            for neigh in dag[node]:
                dfs(neigh)
            # result.append(node)
            path.remove(node)
            # visited.add(node)


        for i in range(numCourses):
            dfs(i)

        return not self.cycleDetected