class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adjList = { i:[] for i in range(n)}

        for start,end in edges:
            adjList[start].append(end)
            adjList[end].append(start)
        
        visited = set()
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour,node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n