
def print_list(a):
    for row in a:
        for element in row:
            print(element, end=' ')
        print()

def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]

def main():
    a = []
    with open('09.02 NumbersList.txt', 'r') as file:
        for line in file:
            a.append(list(map(int, line.split())))
    
    print_list(a)
    
    columns_to_swap = input("Enter the columns to swap: ").split()
    col1 = int(columns_to_swap[0])
    col2 = int(columns_to_swap[1])
    
    swap_columns(a, col1, col2)
    print() # Add a newline for better formatting
    print_list(a)

if __name__ == "__main__":
    main()