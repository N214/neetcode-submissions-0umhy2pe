class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for (crs, pre) in prerequisites:
            graph[crs].append(pre)
        print(f"{graph=}")
        
        output = []
        visited_stack = set()
        done = set()
        def dfs(crs):
            if crs in visited_stack:
                return False
            if crs in done:
                return True
            visited_stack.add(crs)
            for node in graph[crs]:
                if not dfs(node):
                    return False
            visited_stack.remove(crs)
            done.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output