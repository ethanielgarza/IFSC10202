def compare_files(fileA, fileB):
    differences = 0
    with open(fileA, 'r') as file1, open(fileB, 'r') as file2:
        line_num = 1
        while True:
            line1 = file1.readline()
            line2 = file2.readline()
            if not line1 and not line2:
                break
            line1_stripped = line1.strip() if line1 else ""
            line2_stripped = line2.strip() if line2 else ""
            
            if line1_stripped != line2_stripped:
                print(f"line: {line_num} - File A {line1_stripped}")
                print(f"line: {line_num} - File B {line2_stripped}")
                differences += 1
            line_num += 1
    print(f"{differences} differences")
compare_files("06.05 CompareFileA.txt", "06.05 CompareFileB.txt")