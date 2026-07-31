from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        visit = set()

        def addCell(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            queue.append([r, c])

        # Add all 0s first
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visit.add((i, j))
        

        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            distance += 1
        


        

