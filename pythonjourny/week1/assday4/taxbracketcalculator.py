income = float(input("Enter your annaual income: $"))

if income <= 10000:
    print("0%")

elif income <= 40000:
    print("10%")

elif income  <=  80000:
    print("20%")

else:
    print("30%")
