class DSU:
    def __init__(self,n):
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
            return True
        if self.Size[pu] < self.Size[pv]:
            pv,pu = pu,pv
        self.Parent[pv] = pu
        self.Size[pu] += pv
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = []
        N = len(edges) + 1
        dsu = DSU(N)
        for n1,n2 in edges:
            if dsu.union(n1,n2):
                ans.append([n1,n2])

        return ans[-1]
        