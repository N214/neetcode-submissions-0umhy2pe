class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We track seen digits for each constraint:
        # - cols[c] holds the digits already seen in column c
        # - rows[r] holds the digits already seen in row r
        # - squares[(r//3, c//3)] holds the digits already seen in the 3x3 sub-box
        # Using defaultdict(set) makes it easy: if a key hasn't appeared yet, it gives an empty set.
        cols = defaultdict(set)     # digits seen in each column
        rows = defaultdict(set)     # digits seen in each row
        squares = defaultdict(set)  # digits seen in each 3x3 sub-box; key is (row_group, col_group)

        for r in range(9):            # iterate over rows
            for c in range(9):        # iterate over columns
                if board[r][c] == ".":
                    continue          # empty cells can be ignored for validity checks

                val = board[r][c]

                # If this value has already appeared in the same row, column, or sub-box -> invalid
                if (val in cols[c]) or (val in rows[r]) or (val in squares[(r//3, c//3)]):
                    return False

                # Record that we've seen this value in the corresponding constraints
                cols[c].add(val)
                rows[r].add(val)
                squares[(r//3, c//3)].add(val)

        return True  # no duplicates found; the board is valid