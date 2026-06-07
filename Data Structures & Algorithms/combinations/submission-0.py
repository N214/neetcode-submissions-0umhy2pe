class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []
        def dfs(i):
            if len(sol) == k:
                res.append(sol[:])
                return
            left = i
            still_need = k - len(sol)
            if left > still_need:
                dfs(i-1)
            sol.append(i)
            dfs(i-1)
            sol.pop()

        dfs(n)
        return res