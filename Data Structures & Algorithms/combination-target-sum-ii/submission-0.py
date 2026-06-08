class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, sol = [], []

        def dfs(index, total):
            if total == target:
                ans.append(sol[:])
                return
            if index >= len(candidates) or total > target:
                return
            
            sol.append(candidates[index])
            dfs(index+1, total+candidates[index])
            sol.pop()
            
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            dfs(next_index, total)

        dfs(0, 0)
        return ans