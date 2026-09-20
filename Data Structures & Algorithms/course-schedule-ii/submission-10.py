class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        p_reqs = {i:[] for i in range(numCourses)}
        in_degrees = {i:0 for i in range(numCourses)}
        for crs,preq in prerequisites:
            p_reqs[crs].append(preq)
            in_degrees[preq] += 1
        
        q = deque()
        for n in range(numCourses):
            if in_degrees[n] == 0:
                q.append(n)
        
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for preq in p_reqs[node]:
                in_degrees[preq] -= 1
                if in_degrees[preq] == 0:
                    q.append(preq)
        if len(order) == numCourses:
            return order[::-1]
        else:
            return []
        
        