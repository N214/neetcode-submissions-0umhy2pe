class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            a , b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        print(f"{graph=}")

        # a / b, a -> b
        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
            q = deque()
            visited = set() # put the visited set inside the function because each call of the function need a fresh start
            q.append([src, 1]) # the queue contains the pair src and the current multiplication, start with 1 as neutral value
            visited.add(src)
            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                for nei, wei in graph[node]:
                    if nei not in visited:
                        q.append([nei, wei * weight])
                        visited.add(nei)
            return -1

        return [bfs(q[0], q[1])for q in queries]