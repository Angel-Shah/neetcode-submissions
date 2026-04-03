# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = l1
        l1Head = l1
        l2Head = l2
        carry = 0
        prevl1 = None
        prevl2 = None

        while l1Head and l2Head:
            currSum = l1Head.val + l2Head.val + carry
            val = currSum%10
            carry = currSum//10
            l1Head.val = val
            prevl1 = l1Head
            prevl2 = l2Head
            l1Head = l1Head.next
            l2Head = l2Head.next

        #both reached end, just need to add node for carry
        if not l1Head and not l2Head:
            if carry != 0:
                prevl1.next = ListNode(carry,None)
            return ans
        
        if l1Head and not l2Head: #l2 is finished, l1 still has
            while l1Head:
                currSum = l1Head.val + carry
                val = currSum%10
                carry = currSum//10
                l1Head.val = val
                prevl1 = l1Head
                l1Head = l1Head.next
            if carry != 0:
                prevl1.next = ListNode(carry,None)
            return ans
        if l2Head and not l1Head:
            prevl1.next = l2Head
            while l2Head:
                currSum = l2Head.val + carry
                val = currSum%10
                carry = currSum//10
                l2Head.val = val
                prevl2 = l2Head
                l2Head = l2Head.next
            if carry != 0:
                prevl2.next = ListNode(carry,None)
            return ans
