# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iterator = ListNode()
        newHead = iterator
        while list1 and list2:
            if list1.val < list2.val:
                iterator.next = list1
                list1 = list1.next
            else:
                iterator.next = list2
                list2 = list2.next
            iterator = iterator.next
        if list1:
            iterator.next = list1
        if list2:
            iterator.next = list2
        
        return newHead.next