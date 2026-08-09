from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        for account in accounts:
            first_email = account[1]
            for e in account[2:]:
                graph[first_email].append(e)
                #print(f"graph key is {first_email} append {e}")
                #print(graph)
                graph[e].append(first_email)
                #print(f"graph key is {e} append {first_email}")
                #print(graph)
        res = []
        visited = set()

        def dfs(node, emails):
            if not node:
                return None
            visited.add(node)
            emails.append(node)
            for nei in graph[node]:
                if not nei in visited:
                    dfs(nei, emails)

        for account in accounts:
            for e in account[1:]:
                if e not in visited:
                    emails = []
                    dfs(e, emails)
                    name = account[0]
                    res.append([name]+sorted(emails))
        return res
            