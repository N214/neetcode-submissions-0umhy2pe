from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])
        print(f"{graph=}")

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                node, weight = q.popleft()
                # a != c
                if node == target:
                    return weight
                for nei, wei in graph[node]:
                    if nei not in visit:
                        q.append([nei, wei * weight])
                        visit.add(nei)
            return -1
        return [bfs(q[0], q[1]) for q in queries]
        