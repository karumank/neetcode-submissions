class Solution:
    def solve(self, board: List[List[str]]) -> None:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or board[r][c] == "X":
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
            
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)

        for j in range(COLS):
            dfs(0, j)
            dfs(ROWS - 1, j)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"
        





        