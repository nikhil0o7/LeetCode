class DSU:
    def __init__(self,n):
        self.Parent = list(range(n))
        self.Size = [1] * n

    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v) -> bool:
        pu = self.Parent[u]
        pv = self.Parent[v]
        if pu == pv:
            return False
        if self.Size[pv] > self.Size[pu]:
            pu,pv = pv,pu
        self.Parent[pv] = pu
        self.Size[pu] += self.Size[pv]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for n1,n2 in edges:
            if not dsu.union(n1 - 1,n2 - 1):
                return [n1,n2]        