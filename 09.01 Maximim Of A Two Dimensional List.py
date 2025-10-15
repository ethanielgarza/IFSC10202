rows, columns = map(int,input("Enter a Number of Rows or Columns: ").split())
matrix = []
for i in range(rows):
    row_data = list(map(int,input("Enter a line of data: ").split()))
    matrix.append(row_data)
for row in matrix:
    print(*row)
max_val = -1
max_row = -1
max_col = -1
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_row = i
            max_col = j
        elif matrix[i][j] == max_val:
            if i < max_row:
                max_row = i 
                max_col = j
            elif i == max_row and j < max_col:
                max_col = j
print(f"The Maxium value {max_val} occurred in row {max_row + 1} column {max_col + 1} ")