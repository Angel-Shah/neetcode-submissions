from heapq import heappush,heappop
class Solution:
    def helper(self,grid: List[List[int]]):
        rows,cols = len(grid),len(grid[0])
        heap = []
        heappush(heap,(grid[0][0],0,0))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set((0,0))
        # print(f"starting off with heap:{heap}")
        while heap:
            weight, r,c = heappop(heap)
            print(f"just popped: ({weight},{r},{c})")
            if r == rows-1 and c == cols-1:
                return weight
            visited.add((r,c))
            print(f"visited:{visited}")
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited:
                    heappush(heap,(max(weight,grid[nr][nc]),nr,nc))
            print(f"heap look lik:{heap}")
            yield
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        heap = []
        heappush(heap,(grid[0][0],0,0))
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        while heap:
            weight, r,c = heappop(heap)
            if r == rows-1 and c == cols-1:
                return weight
            # visited.add((r,c))
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                # if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited:
                #     heappush(heap,(max(weight,grid[nr][nc]),nr,nc))
                if min(nr,nc)<0 or nr == rows or nc == cols or (nr,nc) in visited:
                    continue
                heappush(heap,(max(weight,grid[nr][nc]),nr,nc))
                visited.add((nr,nc))



        # generator = self.helper(grid)
        # for i in range(6):
        #     next(generator)
        # return -1