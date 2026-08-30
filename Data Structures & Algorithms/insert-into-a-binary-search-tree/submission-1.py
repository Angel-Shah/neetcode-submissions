# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insert(node, target):
            if not node:
                return TreeNode(target)

            if node.left and target < node.val:
                insert(node.left,target)
            if node.right and target > node.val:
                insert(node.right,target)
            if not node.left and target < node.val:
                node.left = insert(node.left,target)
            if not node.right and target > node.val:
                node.right = insert(node.right,target)

        insert(root,val)
        return root