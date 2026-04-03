# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxVal):
            if not node:
                return 0
            res = 0
            if node.val >= maxVal:
                res = 1
            maxVal = max(maxVal, node.val)
            leftAns = dfs(node.left,maxVal)
            rightAns = dfs(node.right,maxVal)
            return res + leftAns + rightAns
        
        return dfs(root,root.val)