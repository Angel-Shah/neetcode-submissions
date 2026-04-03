# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(nodeP,nodeQ):
            if not nodeP and nodeQ:
                return False
            elif not nodeQ and nodeP:
                return False
            elif not nodeP and not nodeQ:
                return True
            else:
                if nodeP.val != nodeQ.val:
                    return False
                
                left = dfs(nodeP.left,nodeQ.left)
                right = dfs(nodeP.right,nodeQ.right)

                return left and right

        return dfs(p,q)