x = float(input("Enter the value of the side: "))
y = float(input("Enter the value of the 2nd side: "))
z = float(input("Enter the value of the 3nd side: "))

if x + y > z and  x + z > y and y + z > x:
    if x == y == z:
        print("Equilateral - all three sides are equal")
    elif x == y or x == z or y == z:
        print("Isosceles - exactly 2 sides are equal")
    elif x != y and x != z or y != z:
        print("Scalene - all 3 sides are different")
else:
    print("Not a triangle")


