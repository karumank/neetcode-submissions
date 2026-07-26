from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rotten_fruits_q = deque([])
        fresh_fruit_count = 0
        minimum_time = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_fruits_q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruit_count += 1
        
        while rotten_fruits_q:
            current_rotten_count = len(rotten_fruits_q)
            rotted_this_round = False
            for i in range(current_rotten_count):
                row, col = rotten_fruits_q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 2
                    rotten_fruits_q.append((nr, nc))
                    fresh_fruit_count -= 1
                    rotted_this_round = True
            if rotted_this_round:
                minimum_time += 1

        if fresh_fruit_count > 0:
            return -1
        
        return minimum_time
                    





