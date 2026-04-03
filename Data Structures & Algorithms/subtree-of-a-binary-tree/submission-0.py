# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            left = self.isSameTree(p.left,q.left)
            right = self.isSameTree(p.right,q.right)
            return left and right
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.potentials = []
        def dfs(node):
            # if node:
            #     print(f"currently at:{node.val}")
            # else:
            #     print("currently at None")
            if not node:
                return
            if node.val == subRoot.val:
                self.potentials.append(node)
            left = dfs(node.left)
            right = dfs(node.right)

        dfs(root) #fill the potentials array

        for pot in self.potentials:
            # print(f"looking at pot:{pot.val}")
            isSame = self.isSameTree(pot,subRoot)
            # print(f"isSame returned :{isSame}")
            if isSame:
                return True
        return False