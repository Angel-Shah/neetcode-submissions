class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        # rank = [1]*(n+1)

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            parent[p2] = p1
            # if rank[p1] >= rank[p2]:
            #     parent[p2] = p1
            #     rank[p1] += rank[p2]
            # else:
            #     parent[p1] = p2
            #     rank[p2] += rank[p1]
            return True
        
        ans = []
        for to,frm in edges:
            if not union(to,frm):
                ans.append([to,frm])
        print(ans)
        return ans[-1]