class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(heights),len(heights[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                if r == (rows-1) or c == (cols-1):
                    atlantic.add((r,c))
        #now do dfs
        def dfs(r,c,pOrA):
            q = deque()
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in dirs:
                nr,nc = r + dr, c + dc

                if ((nr,nc) not in pOrA and
                    nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    heights[nr][nc] >= heights[r][c]):
                    pOrA.add((nr,nc))
                    dfs(nr,nc,pOrA)
            return


        for r,c in list(pacific):
            dfs(r,c,pacific)
        for r,c in list(atlantic):
            dfs(r,c,atlantic)
        both = pacific & atlantic
        print(f"both:{both}")
        return list(both)
