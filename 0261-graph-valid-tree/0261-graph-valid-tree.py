class DSU:
    def __init__(self,n):
        self.comps = n
        self.Parent = list(range(n))
        self.Size = [1] * (n) 

    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.comps -= 1
        if self.Size[pv] < self.Size[pu]:
            pv,pu = pu,pv
        self.Size[pu] += self.Size[pu]
        self.Parent[pv] = pu

        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)

        for u,v in edges:
            if not dsu.union(u,v):
                return False

        return dsu.components() == 1

        


        