class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # dag = {}
        # for i in range(numCourses):
        #     dag[i] = []
        # for preq, crs in prerequisites:
        #     dag[crs].append(preq)
        

        # def dfs(findNode,currNode):
        #     if currNode == findNode:
        #         return True
         
        #     for nei in dag[currNode]:
        #          if dfs(findNode, nei):
        #             return True
        #     return False
        
        # result = []
        
        # for preq,crs in queries:
        #     result.append(dfs(preq,crs))
        
        # return result
        adj = [[] for i in range(numCourses)]
        indegrees = [0]*numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegrees[b] += 1
        prereqs = defaultdict(set) # key: value -> node: its prereqs
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for nei in adj[node]:
                prereqs[nei].add(node)
                prereqs[nei].update(prereqs[node]) # add all prereqs of node to the next node
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        res = []
        for u, v in queries:
            res.append(u in prereqs[v])
        return res