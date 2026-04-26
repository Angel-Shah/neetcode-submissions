# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self,node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        dummy = ListNode(0)
        curr = dummy
        minHeap = []
        for lst in lists:
            heapq.heappush(minHeap,NodeWrapper(lst))

        while minHeap:
            minNode = heapq.heappop(minHeap)
            curr.next = minNode.node
            curr = curr.next

            if minNode.node.next:
                heapq.heappush(minHeap,NodeWrapper(minNode.node.next))
        
        return dummy.next