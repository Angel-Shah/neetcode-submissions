"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(rS,rE,cS,cE):

            # print(f"now checking grid[{rS}][{cS}]")
            val = grid[rS][cS]

            # if rS == rE and cS == cE:

            foundDiffVal = False
            for r in range(rS,rE+1):
                for c in range(cS,cE+1):
                    if grid[r][c] != val:
                        # print(f"val is:{val}, but grid[{r}][{c}] = {grid[r][c]}")
                        foundDiffVal = True
                        break
                if foundDiffVal:
                    break
            # print(f"foundDiffVal is {foundDiffVal}")
            if not foundDiffVal:
                return Node(val,True,None,None,None,None)

            halfRow = (rS+rE)//2
            halfCol = (cS+cE)//2

            # print("going topLeft")
            topLeft = dfs(rS,halfRow,cS,halfCol)
            # print("finished topLeft")

            # print("going topRight")
            topRight= dfs(rS,halfRow,halfCol+1,cE)
            # print("finished topRight")

            # print("going bottomLeft")
            bottomLeft= dfs(halfRow+1,rE,cS,halfCol)
            # print("finished bottomLeft")

            # print("going bottomRight")
            bottomRight= dfs(halfRow+1,rE,halfCol+1,cE)
            # print("finished bottomRight")


            return Node(val,False,topLeft,topRight,bottomLeft,bottomRight)
        
        return dfs(0,len(grid)-1,0,len(grid[0])-1)

