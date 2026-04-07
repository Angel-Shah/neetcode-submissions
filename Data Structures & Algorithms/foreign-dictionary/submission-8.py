from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        # if len(words) <= 1:
        #     if len(words) == 0:
        #         return ""
        #     if len(words) == 1:
        #         return words[0]
        # totalSet = set()
        for i in range(len(words)-1):
            curr,nxt = words[i],words[i+1]
            # currSet = set(curr)
            # nxtSet = set(nxt)
            # totalSet |= currSet
            # totalSet |= nxtSet
            minLen = min(len(curr),len(nxt))
            if len(curr) > len(nxt) and curr[:minLen] == nxt[:minLen]:
                return ""
            for j in range(minLen):
                if curr[j] != nxt[j]:
                    adj[curr[j]].add(nxt[j])
                    break
        print(adj)
        
        self.result = ""
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            self.result += node
            path.remove(node)
            visited.add(node)
            return True
        
        for key in adj:
            if not dfs(key):
                return ""
        return self.result[::-1]