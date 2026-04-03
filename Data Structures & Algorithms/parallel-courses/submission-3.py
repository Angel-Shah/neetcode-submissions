class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {}
        in_count = {}
        visited = set()
        for i in range(1,n+1):
            graph[i] = []
            in_count[i] = 0

        for prev,next in relations:
            graph[prev].append(next)
            in_count[next] += 1
        
        q = []
        for i in range(1,n+1):
            if in_count[i] == 0:
                q.append(i)
        
        semester = 0
        studied = 0

        while q:
            semester += 1
            newQ = []
            for crs in q:
                studied +=1
                for nxt in graph[crs]:
                    in_count[nxt] -= 1
                    if in_count[nxt] == 0:
                        newQ.append(nxt)
            q = newQ
        if studied == n:
            return semester
        else:
            return -1