# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.bstArr = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.bstArr.append(curr)
                curr = curr.right
        # print(f"bstArr look like: {self.bstArr}")
        # for node in self.bstArr:
        #     print(node.val)
        self.pointer = -1
        # print(f"self.pointer is at :{self.pointer.val}, left:{self.pointer.left}, right:{self.pointer.right.val}")


    def next(self) -> int:
        self.pointer += 1
        return self.bstArr[self.pointer].val

    def hasNext(self) -> bool:
        return self.pointer != len(self.bstArr)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()