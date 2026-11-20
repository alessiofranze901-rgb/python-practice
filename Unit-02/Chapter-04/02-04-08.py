side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1:
    if side1 != side2 and side1 != side3 and side2 != side3:
        print("scalene")
    elif side1 == side2 and side1 == side3 and side2 == side3:
        print("equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("isosceles")
else:
    print("not a triangle")

    