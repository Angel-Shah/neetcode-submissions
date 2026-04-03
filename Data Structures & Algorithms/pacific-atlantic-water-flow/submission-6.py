class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(heights),len(heights[0])

        #filling pacific/atlantic sets with inital ocean bordering points
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                if r == (rows-1) or c == (cols-1):
                    atlantic.add((r,c))

        #helper dfs function
        def dfs(r,c,pOrA):
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in dirs:
                nr,nc = r + dr, c + dc

                if ((nr,nc) not in pOrA and
                    nr >= 0 and nr < rows and
                    nc >= 0 and nc < cols and
                    heights[nr][nc] >= heights[r][c]):
                    pOrA.add((nr,nc))
                    dfs(nr,nc,pOrA)

        #populate pacific set with dfs
        for r,c in list(pacific):
            dfs(r,c,pacific)

        #populate atlantic set with dfs
        for r,c in list(atlantic):
            dfs(r,c,atlantic)
        #finding intersection of both sets to find points that can reach both pacific and atlantic
        both = pacific & atlantic
        return list(both)
