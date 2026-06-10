class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        def dfs(open, closed):
            if open == closed == n:
                res.append("".join(sol))
                return
            if open < n:
                sol.append("(")
                dfs(open+1, closed)
                sol.pop()
            if closed < open:
                sol.append(")")
                dfs(open, closed+1)
                sol.pop()

        dfs(0, 0)
        return res