class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #Kahn's algo toposort
        indegrees = {}
        graph = {}
        for n in range(numCourses):
            indegrees[n] = 0
            graph[n] = []
        
        for crs,pre in prerequisites:
            graph[pre].append(crs)
            indegrees[crs] += 1
        
        q = deque()
        topo = []

        #initialize the queue
        for crs,deg in indegrees.items():
            if deg == 0:
                q.append(crs)
        
        while q:
            curr_crs = q.popleft()
            topo.append(curr_crs)
            for nei in graph[curr_crs]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        if len(topo) == numCourses:
            return topo
        else:
            return []


        