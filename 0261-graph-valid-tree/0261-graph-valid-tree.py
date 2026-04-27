class DSU:
    def __init__(self,n):
        self.Parent = list(range(n))
        self.Size = [1] * n
        self.components = n

    def find(self,node) -> int:
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v) -> bool: 
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pv] > self.Size[pu]:
            pu,pv = pv,pu
        self.components -= 1
        self.Parent[pv] = pu
        self.Size[pu] += pv
        return True

    def getComponents(self):
        return self.components
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        for n1,n2 in edges:
            if not dsu.union(n1,n2):
                return False
        return dsu.getComponents() == 1
        