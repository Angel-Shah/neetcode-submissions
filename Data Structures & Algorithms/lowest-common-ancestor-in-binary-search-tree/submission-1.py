# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.LCA = None
        def dfs(node):
            if not node:
                return
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
            elif p.val < node.val and q.val < node.val:
                dfs(node.left)
            else:
                self.LCA = node
                return
        dfs(root)
        return self.LCA