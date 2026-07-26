class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def bfs(r, c):
            queue = [(r, c)]
            grid[r][c] = "0"

            while queue:
                row, col = queue.pop(0)
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == "0"):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands