# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            only_l_or_r = max(left,right) + node.val
            only_node = node.val
            all_sum = left+right+node.val

            currSum = max(only_l_or_r,only_node,all_sum)

            self.maxSum = max(self.maxSum, currSum)

            if currSum == all_sum:
                return only_l_or_r
            else:
                return currSum

        dfs(root)
        return self.maxSum