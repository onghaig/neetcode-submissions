class ListNode():
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LinkedList():
    def __init__(self):
        self.head = ListNode()
        self.curr = None
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
# put the most recently used at the end of the list
class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.cacheTable = {}
        # cache table will point directly to nodes
        self.LinkedList = LinkedList()
    def put(self,key,value):
        # insert a key and value into the cache
        if (key in self.cacheTable):
            node = self.cacheTable[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            lastReal = self.LinkedList.tail.prev
            lastReal.next = node
            node.prev = lastReal
            node.next = self.LinkedList.tail
            self.LinkedList.tail.prev = node
            self.curr = node
            return
        if self.capacity <= 0:
            return False
        self._evict(True)
        newNode = ListNode(key,value)
        lastReal = self.LinkedList.tail.prev
        lastReal.next = newNode
        newNode.prev = lastReal
        newNode.next = self.LinkedList.tail
        self.LinkedList.tail.prev = newNode
        # insert into list
        self.curr = newNode
        self.cacheTable[key] = newNode

    def get(self, key):
        if key in self.cacheTable:
            node = self.cacheTable[key]
            value = node.val 
            node.prev.next = node.next
            node.next.prev = node.prev
            lastReal = self.LinkedList.tail.prev
            lastReal.next = node
            node.prev = lastReal
            node.next = self.LinkedList.tail
            self.LinkedList.tail.prev = node
            self.curr = node
            return value
        else:
            return -1
    def _evict(self, putCall=False):
        if putCall:
            while len(self.cacheTable) >= self.capacity:
                # gotta do allat work
                toRemove = self.LinkedList.head.next
                key = toRemove.key
                val = toRemove.val
                toRemove.prev.next = toRemove.next
                toRemove.next.prev = toRemove.prev
                del self.cacheTable[key]
        else:
            while len(self.cacheTable) > self.capacity:
                toRemove = self.LinkedList.head.next
                key = toRemove.key
                val = toRemove.val
                toRemove.prev.next = toRemove.next
                toRemove.next.prev = toRemove.prev
                del self.cacheTable[key]
        return True
    def _remove(self,key):
        if key not in self.cacheTable:
            return
        toRemove = self.cacheTable[key]
        next = toRemove.next
        prev = toRemove.prev
        next.prev = prev
        prev.next = next
        del self.cacheTable[key]