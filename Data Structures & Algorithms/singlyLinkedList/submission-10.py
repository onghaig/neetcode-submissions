class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        node = self.head
        for _ in range(index):
            if node == None:
                return -1
            node = node.nxt
        if node == None:
            return -1
        return node.val

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        newNode = Node(val)
        newNode.nxt = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        cur = self.head
        if not cur:
            return 
        while cur.nxt:
            cur = cur.nxt
        cur.nxt = Node(val)

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if (index == 0):
            self.head = self.head.nxt
            return True
        node = self.head
        prev = None
        for _ in range(index):
            if node == None:
                return False
            prev = node
            node = node.nxt
        if node == None:
            return False
        prev.nxt = node.nxt
        return True

    def getValues(self) -> List[int]:
        res = []
        node = self.head
        while node:
            if node == None:
                break
            res.append(node.val)
            node = node.nxt
        return res

class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None