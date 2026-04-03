# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return depth
            maxLeft = dfs(node.left,depth +1)
            maxRight = dfs(node.right, depth +1)

            return max(maxLeft,maxRight)

        return dfs(root,0)