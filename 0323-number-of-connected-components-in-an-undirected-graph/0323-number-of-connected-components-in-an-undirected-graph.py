class DSU:
    def __init__(self,n):
        self.Parent = list(range(n))
        self.Size = [1] * (n)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v) -> int:
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: 
            return 0
        if self.Size[pu] < self.Size[pv]:
            pu,pv = pv,pu
        self.Parent[pv] = pu
        self.Size[pu] += self.Size[pv]
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = n
        dsu = DSU(n)
        for n1, n2 in edges:
            ans -= dsu.union(n1,n2)

        return ans











        


        