"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        old_to_new = {}
        queue = deque()
        queue.append(node)
        while queue:
            for x in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node not in old_to_new:
                    new_node = Node(curr_node.val)
                    old_to_new[curr_node] = new_node
                for nei in curr_node.neighbors:
                    if nei not in old_to_new:
                        new_nei = Node(nei.val)
                        old_to_new[nei] = new_nei
                        queue.append(nei)
                    old_to_new[curr_node].neighbors.append(old_to_new[nei])
        
        return old_to_new[node]
                    
