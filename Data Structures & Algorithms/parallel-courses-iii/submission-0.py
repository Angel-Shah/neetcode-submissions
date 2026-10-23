class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = {i:[] for i in range(n)}
        in_degrees = {i:0 for i in range(n)}
        
        max_times = [t for t in time]
        for before,after in relations:
            before,after = before-1,after-1
            graph[before].append(after)
            in_degrees[after] += 1
        
        q = []
        for node in in_degrees:
            if in_degrees[node] == 0:
                q.append(node)
        
        while q:
            new_q = []
            for node in q:
                for nei in graph[node]:
                    in_degrees[nei] -= 1
                    max_times[nei] = max(max_times[nei], max_times[node] + time[nei])
                    if in_degrees[nei] == 0:
                        new_q.append(nei)
            q = new_q
        
        return max(max_times)
        
        