class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        rows,cols = len(image), len(image[0])
        # perform a dfs starting from image[sr][sc]
        def dfs(r,c,image,src_color,visited):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or image[r][c] != src_color:
                return
            
            image[r][c] = color
            visited.add((r,c))

            dfs(r+1,c,image,src_color,visited)
            dfs(r-1,c,image,src_color,visited)
            dfs(r,c+1,image,src_color,visited)
            dfs(r,c-1,image,src_color,visited)

            visited.remove((r,c))
        
        dfs(sr,sc,image,src_color,set())
        return image

