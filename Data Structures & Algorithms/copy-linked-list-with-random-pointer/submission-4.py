"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        # ADD COPY OF NODE 1 BW NODE 1 AND NODE 2... and so on
        curr = head
        while curr:
            temp = curr.next
            curr.next = Node(curr.val, temp)
            curr = temp

        copyhead = head.next
        

        # ASSIGN RANDOM FOR COPIED NODES
        curr = head
        
        while curr:
            copynode = curr.next
            copynode.random = curr.random.next if curr.random else None
            curr = curr.next.next
        

        # DETACH COPIED LINKED LIST AND OG LINKED LIST
        curr  = head
        copycurr = head.next

        while copycurr:
            curr.next = copycurr.next
            copycurr.next = curr.next.next if curr.next else None
            curr = curr.next
            copycurr = copycurr.next
        
        return copyhead
        