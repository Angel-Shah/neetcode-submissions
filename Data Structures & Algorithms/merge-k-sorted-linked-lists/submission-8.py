# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        heap = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))

        dummy = ListNode()
        curr = dummy

        while heap:
            min_val,idx,min_node = heapq.heappop(heap)
            curr.next = min_node
            curr = curr.next
            if min_node.next:
                heapq.heappush(heap,(min_node.next.val,idx,min_node.next))

        return dummy.next