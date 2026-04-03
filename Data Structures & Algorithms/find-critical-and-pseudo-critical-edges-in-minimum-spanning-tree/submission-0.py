class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda x : x[2])

        mst_weight = 0
        uf = UnionFind(n)

        for a,b,w,idx in edges:
            if uf.union(a,b):
                mst_weight += w
        
        critical,psuedo = [],[]


        for a,b,w,idx in edges:
            curr_mst_weight = 0
            uf = UnionFind(n)
            #first we try to find the critical edges
            for a2,b2,w2,idx2 in edges:
                if idx2 != idx and uf.union(a2,b2):
                    curr_mst_weight += w2
            #if current weight excluding the edge is greater than mst_weight, then we found a critical edge
            if max(uf.rank) != n or curr_mst_weight > mst_weight:
                critical.append(idx)
                continue
            
            #if not critical edge, we now check for psuedo
            uf = UnionFind(n)
            uf.union(a,b) # forcing (a2,b2) edge to be in mst to check for psuedo
            curr_mst_weight = w # since we are forcing this edge to be in mst
            for a2,b2,w2,idx2 in edges:
                if uf.union(a2,b2):
                    curr_mst_weight += w2

            if curr_mst_weight == mst_weight:
                #we found a psuedo
                psuedo.append(idx)

        return [critical,psuedo]
