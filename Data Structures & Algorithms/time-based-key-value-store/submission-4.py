class TimeMap:

    def __init__(self):
        # unique single key (there is a global set of keys)
        # hmap = {(k,t) : value}
        self.hmap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((value,timestamp)) 
        else:
            self.hmap[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # use binary search
        res = ""
        arr = self.hmap.get(key,[])
        l = 0
        r = len(arr) - 1
        while (l <= r):
            mid = (l + r)//2
            if (arr[mid][1] == timestamp):
                return arr[mid][0]
            if (arr[mid][1] > timestamp):
                r = mid  - 1
                continue
            else:
                res = arr[mid][0]
                l = mid + 1
                continue
        return res
