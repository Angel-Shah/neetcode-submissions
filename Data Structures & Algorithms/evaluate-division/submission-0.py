class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i , eq in enumerate(equations):
            a,b = eq
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
    
        def bfs(src,target):
            if src not in adj or target not in adj:
                return -1
            q=deque()
            visited = set()
            visited.add(src)
            q.append((src,1))

            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                for n,w in adj[node]:
                    if n not in visited:
                        q.append((n, w * weight))
                        visited.add(n)
            return -1
        
        return [bfs(a,b) for a,b in queries]