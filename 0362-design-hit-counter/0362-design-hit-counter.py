class HitCounter:

    def __init__(self):
        self.total = 0
        self.hits = deque() #[timestamp,count]
        

    def hit(self, timestamp: int) -> None:
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp,1])
        else:
            self.hits[-1][1] += 1
        self.total +=1 

    def getHits(self, timestamp: int) -> int:
        while self.hits:
            diff = timestamp - self.hits[0][0]

            if diff >= 300:
                old_timestamp, old_count = self.hits.popleft()
                self.total -= old_count
            else:
                break


        return self.total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)