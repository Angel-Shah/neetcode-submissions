# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        # ans = l1
        # l1Head = l1
        # l2Head = l2
        # carry = 0
        # prevl1 = None
        # prevl2 = None

        # while l1Head and l2Head:
        #     currSum = l1Head.val + l2Head.val + carry
        #     val = currSum%10
        #     carry = currSum//10
        #     l1Head.val = val
        #     prevl1 = l1Head
        #     prevl2 = l2Head
        #     l1Head = l1Head.next
        #     l2Head = l2Head.next

        # #both reached end, just need to add node for carry
        # if not l1Head and not l2Head:
        #     if carry != 0:
        #         prevl1.next = ListNode(carry,None)
        #     return ans
        
        # if l1Head and not l2Head: #l2 is finished, l1 still has
        #     while l1Head:
        #         currSum = l1Head.val + carry
        #         val = currSum%10
        #         carry = currSum//10
        #         l1Head.val = val
        #         prevl1 = l1Head
        #         l1Head = l1Head.next
        #     if carry != 0:
        #         prevl1.next = ListNode(carry,None)
        #     return ans
        # if l2Head and not l1Head:
        #     prevl1.next = l2Head
        #     while l2Head:
        #         currSum = l2Head.val + carry
        #         val = currSum%10
        #         carry = currSum//10
        #         l2Head.val = val
        #         prevl2 = l2Head
        #         l2Head = l2Head.next
        #     if carry != 0:
        #         prevl2.next = ListNode(carry,None)
        #     return ans
