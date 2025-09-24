def diameter(radius):
    return 2 * radius
import math
def circumfrence (radius):
    circumfrence = 2 * math.pi * radius
    return circumfrence
def area(radius):
    area = math.pi *(radius ** 2)
    return area

def main():

    print(f"{'diameter'}:>15 {'circumfrence'}:>15 {'area'}:>15")
    print("_" * 63)
try:
    with open("06.01 Radius.txt") as file:
        for line in file:
            try:
                radius = float(line.strip())

                diam = diameter(radius)
                circ = circumfrence(radius)
                circle_area = area(radius)

                print(f"{radius:>15.5f} {diam:>15.5f} {circ:>15.5f} {circle_area:>15.5f}")
                
            except ValueError:
          # Handle cases where a line is not a valid number
                print(f"Skipping invalid data: {line.strip()}")

except FileNotFoundError:
    print("Error: The file '06.01 Radius.txt' was not found.")

if __name__ == "__main__":
  main()