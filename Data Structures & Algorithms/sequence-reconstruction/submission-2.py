class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        edges = {n:[] for n in nums}
        indegrees = {n:0 for n in nums}
        for seq in sequences:
            for i in range(len(seq)-1):
                u = seq[i]
                v = seq[i+1]
                edges[u].append(v)
                indegrees[v] += 1
        
        q = deque()
        for n,deg in indegrees.items():
            if deg == 0:
                q.append(n)
        
        idx = 0
        while q:
            q_len = len(q)
            node = q.popleft()
            if q_len != 1 or node != nums[idx]:
                return False
            for nei in edges[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
            idx += 1
        
        return True

