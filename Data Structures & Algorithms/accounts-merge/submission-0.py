from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 1. Create a graph where emails are nodes and all emails in a account are connected
        # 2. Go through all emails and find connected components using DFS
        graph = defaultdict(list)
        for i, acc in enumerate(accounts):
            first_email = acc[1]
            for e in acc[2:]:
                graph[first_email].append(e)
                graph[e].append(first_email)
        print(f"{graph=}")
        visit = set()
        res = []

        def dfs(node, comp):
            visit.add(node)
            comp.append(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei, comp)
        
        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                print(f"{e=}")
                if e not in visit:
                    components = []
                    dfs(e, components)
                    name = acc[0]
                    res.append([name]+sorted(components))
        print(f"{res=}")
        return res