# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        result =[]
        stack = []
        visited = set()
        curr = root
        while curr or stack:
            if curr:
                if curr in visited:
                    result.append(curr.val)
                    if stack:
                        curr = stack.pop()
                    else:
                        curr = None
                else:
                    stack.append(curr)
                    visited.add(curr)
                    if curr.right:
                        stack.append(curr.right)
                    curr = curr.left
            else:
                curr = stack.pop()
                # result.append(curr.val)
                # visited.add(curr)
        return result