from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col,0))
                elif grid[row][col] == 1:
                    fresh_count+=1

        if fresh_count == 0:
            return 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        while queue:
            r, c, minutes = queue.popleft()
            for dr,dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc, minutes + 1))
        return -1 if fresh_count > 0 else minutes
        