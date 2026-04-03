# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def printList(self,head):
        ans = []
        curr = head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        print(ans)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversedHead = self.reverseList(head)
        curr = reversedHead
        count = 1
        # print(f"reversed list before pop:{self.printList(reversedHead)}")
        
        if n == 1:
            reversedHead = reversedHead.next
        else:
            while curr:
                if count+1 == n:
                    curr.next = curr.next.next
                    break
                curr = curr.next
                count +=1
        # print(f"After pop:{self.printList(reversedHead)}")
        return self.reverseList(reversedHead)
