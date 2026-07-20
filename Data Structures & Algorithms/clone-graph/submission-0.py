"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # do dfs, if we find a new node we add it, mark it as visited, and then continue
        cloned = {}

        def dfs(node):
            if (not node): return None
            if (node.val in cloned):
                return cloned[node.val]
            clone = Node(node.val, [])
            cloned[node.val] = clone
            for neighbor in node.neighbors:
                # index is neighbor.val
                if (neighbor.val in cloned):
                    clone.neighbors.append(cloned[neighbor.val])
                else:
                    clone.neighbors.append(dfs(neighbor)) 
            # add cloned to the table
            return clone
        
        return dfs(node)