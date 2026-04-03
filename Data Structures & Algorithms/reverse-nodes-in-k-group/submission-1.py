# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#have a slow/fast pointer
#move fast pointer k times to know where to stop
# move slow and keep reversing until you hit fast
# if you are trying to move fast k-times and you hit end of linked list
# then we know that there are < k remaining, leave the rest as is

class Solution:
    # def printLinkedList(self,head):
    #     curr = head
    #     ans = []
    #     while curr:
    #         ans.append(curr.val)
    #         curr = curr.next
    #     return ans
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy = ListNode()
        # dummy.next = head
        slow = fast = head
        prev = None
        newHead = head
        isFirstTime = True
        while True:
            check = fast
            for i in range(k):
                if not check:
                    return newHead
                check = check.next

            # print(f"Moved fast k-times, slow:{slow.val}, fast:{fast.val or None}")
            # reverst slow as we move it forwards
            tail = slow
            group_prev = None
            for j in range(k):
                nxt = slow.next
                slow.next = group_prev
                group_prev = slow
                slow = nxt
            
            if isFirstTime:
                newHead = group_prev
                isFirstTime = False
            else:
                prev.next = group_prev
            
            tail.next = slow
            prev = tail
            fast = slow

        return newHead
