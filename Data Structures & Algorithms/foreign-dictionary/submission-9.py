from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        if len(words) <= 1:
            if len(words) == 0:
                return ""
            if len(words) == 1:
                return words[0]
        totalSet = set()
        for i in range(len(words)-1):
            curr,nxt = words[i],words[i+1]
            currSet = set(curr)
            nxtSet = set(nxt)
            totalSet |= currSet
            totalSet |= nxtSet
            x = 0
            while x < len(curr) and x < len(nxt) and curr[x] == nxt[x]:
                x += 1
            if x >= len(nxt) and x < len(curr):
                return ""
            if x < len(curr) and x < len(nxt):
                if nxt[x] in adj:
                    adj[nxt[x]].append(curr[x])
                else:
                    adj[nxt[x]] = [curr[x]]
        print(adj)
        # print(totalSet)

        inDegrees = {char:0 for char in totalSet}
        for c in totalSet:
            # inDegrees[c] = 0
            for nei in adj.get(c,[]):
                inDegrees[nei] += 1

        print(inDegrees)
        result = ""
        q = deque()
        for key in inDegrees:
            if inDegrees[key] == 0:
                q.append(key)
        # print(q)

        while q:
            curr = q.popleft()
            result += curr
            for nei in adj.get(curr,[]):
                inDegrees[nei] -= 1
                if inDegrees[nei] == 0:
                    q.append(nei)
            
        if len(result) < len(totalSet):
            return ""
        return result[::-1]