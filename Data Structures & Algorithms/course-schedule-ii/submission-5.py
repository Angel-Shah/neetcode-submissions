class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c:[] for c in range(numCourses)}
        indegrees = [0]*numCourses
        for crs,pre in prerequisites:
            adj[pre].append(crs)
            indegrees[crs] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        output = []
        while q:
            course = q.popleft()
            output.append(course)
            for nei in adj[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        if len(output) != numCourses:
            return []
        else:
            return output
        
