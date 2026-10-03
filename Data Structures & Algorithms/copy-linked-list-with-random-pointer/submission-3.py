"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        copy = Node(0)
        copyHead = copy
        mapping = {}
        # node.val -> node.random.val
        copyNodes = {}
        nodetocopy = {}
        while node:
            copy.next = Node(node.val)
            copy = copy.next
            nodetocopy[node] = copy
            mapping[copy] = node.random if node.random else None
            copyNodes[copy] = copy
            node = node.next
        copy = copyHead.next
        while copy:
            random = mapping[copy]
            originalNode = nodetocopy[random] if random in nodetocopy else None
            copy.random = copyNodes[originalNode] if originalNode else None
            copy = copy.next

        return copyHead.next