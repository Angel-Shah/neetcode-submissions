"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# class Solution:
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if not root:
#             return root
#         queue = deque()
#         queue.append(root)
#         while queue:
#             for i in range(len(queue)-1):
#                 if i+1 <= len(queue):
#                     queue[i].next = queue[i+1]

#             for j in range(len(queue)):
#                 popped = queue.popleft()
#                 if popped.left and popped.right:
#                     queue.append(popped.left)
#                     queue.append(popped.right)
#         return root

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur, nxt = root, root.left if root else None

        while nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left

        return root