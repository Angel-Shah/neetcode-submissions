class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ans = float('-inf')
        rows,cols = len(heights),len(heights[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        minHeap = [(0,0,0)]
        visited = set()

        while minHeap:
            cost,r,c = heapq.heappop(minHeap)
            visited.add((r,c))
            ans = max(ans,cost)

            if r == rows-1 and c == cols-1:
                return ans

            for dr,dc in dirs:
                nr,nc = r + dr, c + dc
                
                if min(nr,nc) >= 0 and nr < rows and nc < cols and (nr,nc) not in visited:
                    n_cost = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(minHeap,(n_cost,nr,nc))