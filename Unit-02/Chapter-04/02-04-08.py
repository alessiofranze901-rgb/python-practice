side1 = float(input())
side2 = float(input())
side3 = float(input())

if side1 + side2 < side3 or side1 + side3 < side2 or  side3 + side2 < side1:
    print("not a triangle")
elif side1 != side2 and side1 != side3 and side2 != side3:
    print("scalene")
elif side1 == side2 and side1 == side3 and side2 == side3:
    print("equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("isosceles")
 