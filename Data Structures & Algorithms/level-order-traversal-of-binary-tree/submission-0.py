# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[root]
        ans = []
        while q:
            newQ = []
            ansAppend = []
            for node in q:
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
                ansAppend.append(node.val)
            ans.append(ansAppend)
            q = newQ
        return ans