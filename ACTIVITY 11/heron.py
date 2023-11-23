import math

def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    print("Enter the lengths of the sides of the triangle:")
    a = float(input("Side 1: "))
    b = float(input("Side 2: "))
    c = float(input("Side 3: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid side lengths. All sides must be greater than zero.")
    else:
        if is_right_triangle(a, b, c):
            print("The triangle is a right-angled triangle.")
        else:
            print("The triangle is not a right-angled triangle.")

        area = calculate_area(a, b, c)
        print(f"The area of the triangle is: {area:.2f}")

if __name__ == "__main__":
    main()
