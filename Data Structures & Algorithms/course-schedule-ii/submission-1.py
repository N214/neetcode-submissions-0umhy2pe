class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        print(f"{graph=}")
        # with the dfs, we want to detect if there's a loop
        visited = set()
        visiting = set()
        res = []
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


        
