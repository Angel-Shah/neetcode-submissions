# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.totalMax = float('-inf')
        def dfs(node, depth):
            if node:
                print(f"currently at: {node.val}")
            else:
                print(f"currently at: {node}")

            if not node:
                print(f"returning: {depth-1}")
                return depth-1
            print(f"going left from :{node.val}")
            maxLeft = dfs(node.left, depth + 1 )
            print(f"done going left from:{node.val}")

            print(f"going right from :{node.val}")
            maxRight = dfs(node.right, depth +1)
            print(f"done going right from: {node.val}")

            # print(f"currently at :{node.val}, total left-right sum:{maxLeft+maxRight + 1}")
            maxRet = max(maxLeft,maxRight)
            # print(f"maxLeft:{maxLeft}, maxRight:{maxRight} ")
            self.totalMax = max(self.totalMax,(maxLeft-depth)+(maxRight-depth))
            return  max(maxLeft,maxRight)
        
        dfs(root,0)

        return self.totalMax