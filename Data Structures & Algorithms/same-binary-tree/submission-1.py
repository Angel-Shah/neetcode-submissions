# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(nodeP,nodeQ):
            if not nodeP and not nodeQ:
                return True
            if nodeP and nodeQ and nodeP.val == nodeQ.val:
                left = dfs(nodeP.left,nodeQ.left)
                right = dfs(nodeP.right,nodeQ.right)
                return left and right
            else:
                return False
                

        return dfs(p,q)