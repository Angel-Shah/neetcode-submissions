class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])

        def dfs(r,c,currSet):
            if(r >= 0 and r < rows and
            c >= 0 and c < cols and
            (r,c) not in currSet):
                if board[r][c] == 'O':
                    currSet.add((r,c))
                    # print(f"in dfs(), added ({r},{c}) to set and set look like:{currSet}")
                    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
                    for dr,dc in dirs:
                        nr,nc = r + dr , c + dc
                        # if ((nr,nc) not in currSet and
                        #     board[nr][nc] == 'O'):
                        dfs(nr,nc,currSet)
            return currSet

        def isSurrounded(islandSet):
            for r,c in islandSet:
                if (r == 0 or r == rows-1 or
                    c == 0 or c == cols-1):
                    return False
            return True
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # print(f"found O at :{r},{c}")
                    island = dfs(r,c,set())
                    if isSurrounded(island):
                        for x,y in island:
                            board[x][y] = 'X'

        