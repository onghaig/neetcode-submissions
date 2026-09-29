class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0 
        self.capacity = capacity
        self.queue = deque()

    def get(self, key: int) -> int:
        if (key not in self.cache):
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if (key in self.cache):
            self.queue.remove(key)
            self.cache[key] = value
            self.queue.append(key)
        else:
            if (self.size >= self.capacity):
                # need to remove smth
                removed = self.queue.popleft()
                del self.cache[removed]
                self.cache[key] = value
                self.queue.append(key)
            else:
                self.cache[key] = value
                self.size += 1
                self.queue.append(key)


