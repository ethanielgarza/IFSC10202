def find_sections(search_term):
    with open("constitution.txt", "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
            if search_term.lower() in line.lower():
                start = i
                while start > 0 and lines[start -1].strip() != "":
                    start -= 1
                end = i 
                while end < len(lines) and lines[end].strip() != "":
                    end += 1

                for j in range(start,end):
                    print("Line:", j, lines[j].strip())
                print()
def main():
     while True:
          search_term = input("Enter search term: ")
          if not search_term:
               break
          find_sections(search_term)
if __name__ == "__main__":
     main()