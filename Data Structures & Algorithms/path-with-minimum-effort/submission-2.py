class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights), len(heights[0])
        minHeap = [[0,0,0]]
        visited = set()
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue
            visited.add((r,c))
            if (r,c) == (rows-1, cols-1):
                return diff
            
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if min(nr,nc) < 0 or nr == rows or nc == cols or (nr,nc) in visited:
                    continue
                n_diff = max(diff,abs(heights[nr][nc] - heights[r][c]))
                heapq.heappush(minHeap,[n_diff,nr,nc])