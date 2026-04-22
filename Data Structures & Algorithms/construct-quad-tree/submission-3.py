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

            val = grid[rS][cS]

            foundDiffVal = False
            for r in range(rS,rE+1):
                for c in range(cS,cE+1):
                    if grid[r][c] != val:
                        foundDiffVal = True
                        break
                if foundDiffVal:
                    break
            if not foundDiffVal:
                return Node(val,True,None,None,None,None)

            halfRow = (rS+rE)//2
            halfCol = (cS+cE)//2

            topLeft = dfs(rS,halfRow,cS,halfCol)

            topRight= dfs(rS,halfRow,halfCol+1,cE)

            bottomLeft= dfs(halfRow+1,rE,cS,halfCol)

            bottomRight= dfs(halfRow+1,rE,halfCol+1,cE)

            return Node(val,False,topLeft,topRight,bottomLeft,bottomRight)
        
        return dfs(0,len(grid)-1,0,len(grid[0])-1)

