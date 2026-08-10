year = int(input("input your year: "))

if year % 4 == 0 and year % 100 != 0:
    print("A leap year")
elif year % 400 == 0:
    print("A leap yeaar")
else:
    print("Not a leap year")

