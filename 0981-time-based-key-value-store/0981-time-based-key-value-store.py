class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        if timestamp < self.store[key][0][0]:
            return ""

        l,r = 0, len(self.store[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.store[key][mid][0] <= timestamp:
                res = self.store[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)