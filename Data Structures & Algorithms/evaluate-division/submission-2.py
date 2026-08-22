class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        print(f"{graph=}")
        # node: each numerator
        # edges: each denominator, and the result 
        # meaning of the edge: division
        # question: ?
        # DFS? 
        
        def dfs(current, target):
            if current == target:
                return 1
            visited.add(current)
            for nei, wei in graph[current]:
                if nei not in visited:
                    res = dfs(nei, target)
                    if res != -1:
                        return wei * res
            return -1

        res = []
        for q in queries:
            visited = set()
            if q[0] not in graph or q[1] not in graph:
                val = -1
            else:
                val = dfs(q[0], q[1])
            res.append(val)
        return res