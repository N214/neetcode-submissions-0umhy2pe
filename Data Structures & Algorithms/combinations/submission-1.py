class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def dfs(start):
            if len(sol) == k:
                res.append(sol[:])
                return
            still_need = k - len(sol)
            for num in range(start, n + 1):
                numbers_left = n - num + 1

                if numbers_left < still_need:
                    break
                sol.append(num)
                dfs(num + 1)
                sol.pop()

        dfs(1)
        return res