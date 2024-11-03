N = int(input("Enter the number of queens: "))
board = [[0] * N for _ in range(N)]

def attack(i, j):
    return any(board[i][k] == 1 or board[k][j] == 1 for k in range(N)) or any(board[k][l] == 1 for k in range(N) for l in range(N) if k + l == i + j or k - l == i - j)

def N_queens(n):
    if n == 0: return True
    for i in range(N):
        for j in range(N):
            if not attack(i, j):
                board[i][j] = 1
                if N_queens(n - 1): return True
                board[i][j] = 0
    return False

N_queens(N)
for row in board: print(row)
