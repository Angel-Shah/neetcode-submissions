class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n)
        

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        parX = self.find(x)
        parY = self.find(y)
        if parX == parY:
            return False
        
        if self.rank[parX] > self.rank[parY]:
            self.parent[parY] = parX
            self.rank[parX] += self.rank[parY]
        else:
            self.parent[parX] = parY
            self.rank[parY] += self.rank[parX]
        return True



    def getNumComponents(self) -> int:
        for i in range(len(self.parent)):
            self.find(i)
        return len(set(self.parent))
