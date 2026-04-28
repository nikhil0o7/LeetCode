class DSU:
    def __init__(self, n):
        self.Parent = list(range(n))
        self.Size = [1] * n

    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pv] > self.Size[pu]:
            pu,pv = pv,pu
        self.Parent[pv] = pu
        self.Size[pu] += self.Size[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        comps = n
        for n1,n2 in edges:
            if dsu.union(n1,n2):
                comps -= 1

        return comps

        