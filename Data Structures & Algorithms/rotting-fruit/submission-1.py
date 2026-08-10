"""
0 = empty
1 = fresh
2 = rotten

if fresh fruit is next to rotten fruit,
fresh fruit becomes rotten after 1 minute

approach: matrix bfs, multi-source bfs

why multi-source bfs?
- all rotten fruits are added to the queue first
- then they all spread level by level / minute by minute

why no visited set?
- because grid[r][c] = 2 marks the cell as visited
- after that, grid[r][c] != 1, so we cannot add it again

T.C. O(m*n)
S.C. O(m*n)
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        fresh = 0
        time = 0

        # first, scan the grid
        # put all rotten fruits into queue
        # count all fresh fruits
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        def bfs():
            nonlocal fresh, time

            # each while loop = one minute
            # continue while rotten fruits can spread
            # and fresh fruits still exist
            while queue and fresh > 0:

                # len(queue) = rotten fruits available
                # at the START of this minute
                #
                # newly rotten fruits are added to queue,
                # but they spread in the NEXT minute
                for _ in range(len(queue)):
                    i, j = queue.popleft()

                    for dr, dc in directions:
                        r = i + dr
                        c = j + dc

                        # skip if:
                        # - out of bounds
                        # - not fresh
                        if (r < 0 or c < 0 or r >= rows or c >= cols
                            or grid[r][c] != 1):
                            continue

                        # mark as rotten
                        # this also works like visited
                        grid[r][c] = 2

                        # one less fresh fruit
                        fresh -= 1

                        # add it to queue so it can spread
                        # in the NEXT minute
                        queue.append((r, c))

                # after all rotten fruits from this level spread,
                # one minute has passed
                time += 1

            # if no fresh fruit left, return total time
            if fresh == 0:
                return time

            # if fresh fruit is still left,
            # it was unreachable
            return -1

        return bfs()