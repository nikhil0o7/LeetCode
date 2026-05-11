class DSU:
    def __init__(self,n):
        self.Parent = [i for i in range(n)]
        self.Rank = [0] * n

    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v) -> bool:
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Rank[pu] < self.Rank[pv]:
            pu,pv = pv,pu
        self.Parent[pv] = pu
        self.Rank[pu] += 1
        return True 

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x : x[0])
        uf = DSU(n)
        group_cnt = n 
        
        for timestamp,friend_a,friend_b in logs:
            if uf.union(friend_a,friend_b):
                group_cnt -= 1

            if group_cnt == 1:
                return timestamp

        
        return -1