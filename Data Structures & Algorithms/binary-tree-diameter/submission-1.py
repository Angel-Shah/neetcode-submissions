# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.totalMax = float('-inf')
        def dfs(node, depth):
            if not node:
                return depth-1
            maxLeft = dfs(node.left, depth + 1 )

            maxRight = dfs(node.right, depth +1)

            maxRet = max(maxLeft,maxRight)
            self.totalMax = max(self.totalMax,(maxLeft-depth)+(maxRight-depth))
            return  max(maxLeft,maxRight)
        
        dfs(root,0)

        return self.totalMax