class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        p_reqs = {i:[] for i in range(numCourses)}
        in_degrees = {i:0 for i in range(numCourses)}
        for crs,preq in prerequisites:
            p_reqs[crs].append(preq)
            in_degrees[preq] += 1
        
        q = deque()
        for n in range(numCourses):
            if in_degrees[n] == 0:
                q.append(n)
        
        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for preq in p_reqs[node]:
                in_degrees[preq] -= 1
                if in_degrees[preq] == 0:
                    q.append(preq)
                    
        return finished == numCourses
        
        