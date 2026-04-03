# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = slow = dummy
        
        def moveKsteps(node):
            print(f"moving {k}-steps from:{node.val}")
            curr = node
            count = k
            while curr and count>0:
                # print(f"curr -> {curr}, count ->")
                curr = curr.next
                count -=1
            return curr

        groupPrev = dummy
        while True:
            fast = moveKsteps(fast)    

            if not fast:
                break
                
            prevGroupEnd = slow
            nxtGroupStart = fast.next

            curr = slow
            tail = slow.next
            prev = None
            while curr != fast:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            curr.next = prev
            slow = curr

            prevGroupEnd.next = slow

            tail.next = nxtGroupStart

            slow = fast = tail

        return dummy.next
