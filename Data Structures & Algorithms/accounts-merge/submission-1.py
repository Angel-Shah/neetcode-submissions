class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIdx = {}
        dsu = DSU(len(accounts))

        for i,accs in enumerate(accounts):
            for email in accs[1:]:
                if email not in emailToIdx:
                    emailToIdx[email] = i
                else:
                    dsu.union(i,emailToIdx[email])
        
        emailGroups = {}

        for email,idx in emailToIdx.items():
            parentIdx = dsu.find(idx)
            if parentIdx in emailGroups:
                emailGroups[parentIdx].append(email)
            else:
                emailGroups[parentIdx] = [email]
        

        result = []

        for index, emails in emailGroups.items():
            name = accounts[index][0]
            result.append([name]+ sorted(emails))
        
        return result


