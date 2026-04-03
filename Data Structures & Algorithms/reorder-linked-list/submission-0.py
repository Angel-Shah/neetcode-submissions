# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the halfway point
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #now slow.next is start of 2nd half, now we reverse it

        second = slow.next
        slow.next = None # detach the first half from second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first,second = head, prev
        while second:
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first= temp1
            second= temp2