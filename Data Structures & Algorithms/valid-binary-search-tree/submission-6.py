# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.isValidTree = True

        def dfs(node,maxL,minR):
            if not node:
                return
            if maxL >= node.val or minR <= node.val:
                self.isValidTree = False
            
            dfs(node.left,maxL,node.val)
            dfs(node.right,node.val,minR)
 
            return node.val
        
        dfs(root,float('-inf'),float('inf'))

        return self.isValidTree

