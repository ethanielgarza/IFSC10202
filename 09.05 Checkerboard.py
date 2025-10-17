n = int(input("Enter size: "))
board = []
frame_row = ["+"] + ["-"] * n + ["+"]
board.append(frame_row)
for _ in range(n):
    interior_row = ["|"] + [" "] * n +["|"]
    board.append(interior_row)
board.append(frame_row)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:
            board[i][j] = "*"
for row in board:
    print("".join(row))