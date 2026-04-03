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
            if p.val == node.val or q.val == node.val:
                self.LCA = node
                return
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
            if p.val < node.val and q.val < node.val:
                dfs(node.left)
            if ((p.val < node.val and q.val > node.val) or
                (q.val < node.val and p.val > node.val)):
                self.LCA = node
                return
        dfs(root)
        return self.LCA