# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head

        while head:
            # slow = slow.next
            # fast = fast.next
            if fast and slow:
                fast = fast.next
                if fast:
                    fast = fast.next
                else:
                    return False
                slow = slow.next
            else:
                return False
            if slow == fast:
                return True
            head = head.next
        return False