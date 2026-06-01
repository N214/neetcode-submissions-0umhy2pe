class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, r, c, i, visited):
            rows, cols = len(board), len(board[0])

            # invalid position, already visited, or char mismatch
            if (min(r, c) < 0 or r >= rows or c >= cols or
                (r, c) in visited or word[i] != board[r][c]):
                return False

            # if current character is the last character, we found the word
            if i == len(word) - 1:
                return True

            # mark current cell as used
            visited.add((r, c))

            # explore 4 directions with next character index
            res = (
                dfs(board, r + 1, c, i + 1, visited) or
                dfs(board, r - 1, c, i + 1, visited) or
                dfs(board, r, c + 1, i + 1, visited) or
                dfs(board, r, c - 1, i + 1, visited)
            )

            # backtrack
            visited.remove((r, c))

            return res

        # need to try starting from every cell, not only (0, 0)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(board, r, c, 0, set()):
                    return True

        return False