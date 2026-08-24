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
        visited = set()

        queue.append(node)
        # visited.add(node)
        while queue:
            for x in range(len(queue)):
                curr_node = queue.popleft()
                print(f"currently processing:{curr_node.val}")
                if curr_node not in old_to_new:
                    print(f"{curr_node.val} is not in old_to_new")
                    new_node = Node(curr_node.val)
                    old_to_new[curr_node] = new_node
                for nei in curr_node.neighbors:
                    print(f"lookign at {curr_node.val}'s neighbour:{nei.val}")
                    if nei not in old_to_new:
                        new_nei = Node(nei.val)
                        old_to_new[nei] = new_nei
                        queue.append(nei)

                    old_to_new[curr_node].neighbors.append(old_to_new[nei])
                    # if nei not in visited:
                    #     print(f"adding {nei.val} to bfs queue and visited set")
                    #     queue.append(nei)
                    #     visited.add(nei)
        return old_to_new[node]
                    
