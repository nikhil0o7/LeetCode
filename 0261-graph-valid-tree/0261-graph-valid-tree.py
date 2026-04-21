class DSU:
    def __init__(self,n):
        self.comps = n
        self.Parent = list(range(n))
        self.Size = [1] * n

    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def getComponents(self):
        return self.comps
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] < self.Size[pv]:
            pu,pv = pv,pu
        self.comps -= 1
        self.Parent[pv] = pu
        self.Size[pu] += pv
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        N = len(edges)
        dsu = DSU(n)
        for n1,n2 in edges:
            if not dsu.union(n1,n2):
                return False
        print(dsu.getComponents())
        return dsu.getComponents() == 1
        