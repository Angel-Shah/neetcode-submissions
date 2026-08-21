class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        if src_color == color:
            return image
        rows,cols = len(image), len(image[0])
        # perform a dfs starting from image[sr][sc]
        def dfs(r,c):
            if min(r,c) < 0 or r ==rows or c == cols or image[r][c] != src_color:
                return
            image[r][c] = color

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image

