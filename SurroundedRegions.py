from typing import List


def bfs(board, i, j, n, m):
    if (i < 0 or j < 0 or i >= n or j >= m or board[i][j] != 'O'):
        return

    board[i][j] = "Y"
    bfs(board, i + 1, j, n, m)
    bfs(board, i, j + 1, n, m)
    bfs(board, i - 1, j, n, m)
    bfs(board, i, j - 1, n, m)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        for i in range(n):
            if (board[i][0] == 'O'):
                bfs(board, i, 0, n, m)

        for i in range(n):
            if (board[i][m - 1] == 'O'):
                bfs(board, i, m - 1, n, m)

        for i in range(m):
            if (board[0][i] == 'O'):
                bfs(board, 0, i, n, m)

        for i in range(m):
            if (board[n - 1][i] == 'O'):
                bfs(board, n - 1, i, n, m)
        # print(board)

        for i in range(n):
            for j in range(m):
                if (board[i][j] == 'O'):
                    board[i][j] = 'X'
                if (board[i][j] == 'Y'):
                    board[i][j] = 'O'




