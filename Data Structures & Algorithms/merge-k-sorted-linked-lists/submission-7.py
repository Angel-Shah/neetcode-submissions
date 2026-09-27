# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val < other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap,NodeWrapper(node))

        dummy = ListNode()
        curr = dummy

        while heap:
            curr_min = heapq.heappop(heap)
            curr.next = curr_min.node
            curr = curr.next
            if curr_min.node.next:
                heapq.heappush(heap,NodeWrapper(curr_min.node.next))

        return dummy.next