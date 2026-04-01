class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        target = len(graph) - 1
        def backtrack(curr_node, curr):
            if curr_node == target:
                ans.append(curr[:])
                return 
            
            for node in graph[curr_node]:
                curr.append(node)
                backtrack(node,curr)
                curr.pop()
        
        backtrack(0, [0])
        return ans