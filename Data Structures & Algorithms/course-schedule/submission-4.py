# class GraphNode:
#     def __init__(self,val):
#         self.val = val
#         self.neighbours = []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dag = {}
        for i in range(numCourses):
            dag[i] = []
        for c,pr in prerequisites:
            dag[c].append(pr)
        
        self.cycleDetected = False
        path = set()

        def dfs(node):
            # if self.cycleDetected:
            #     return
            if node in path:
                self.cycleDetected = True
                return

            path.add(node)
            
            for neigh in dag[node]:
                dfs(neigh)
                
            path.remove(node)


        for i in range(numCourses):
            dfs(i)

        return not self.cycleDetected