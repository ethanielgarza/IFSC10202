def percentchange(todaysprice,yesterdaysprice):
    return ((todaysprice - yesterdaysprice) / yesterdaysprice) * 100

def main():
    file_name = "06.02 Stock.txt"
    print(f"{'Price':>10} {'Change':>15} ")

    with open(file_name, "r") as file:
        yesterdaysprice = float(file.readline())
        print(f"{yesterdaysprice:>10.2f}")

        for line in file:
            todayprice = float(line)
            change = percentchange(todayprice, yesterdaysprice)
            print(f"{todayprice:>10.2f} {change:>15.2f}%")
            yesterdaysprice = todayprice
if __name__ == "__main__":
    main()