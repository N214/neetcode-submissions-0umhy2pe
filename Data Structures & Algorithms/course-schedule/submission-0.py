class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first build the graph
        # build dfs 
        # iterate through the range num courses
        graph = defaultdict(list)
        for (crs, pre) in prerequisites:
            graph[crs].append(pre)

        visited_stack = set()
        seen = set()

        def dfs(crs):
            # return true if course can be finished
            if crs in visited_stack:
                return False
            if crs in seen:
                return True
            # core of the dfs
            visited_stack.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visited_stack.remove(crs)
            seen.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True