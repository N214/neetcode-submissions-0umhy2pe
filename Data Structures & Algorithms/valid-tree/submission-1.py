from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False 
            visited.add(node)
            for j in graph[node]:
                if j == prev:
                    continue
                if not dfs(j, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n