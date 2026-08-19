number = int(input("Enter your number: "))

if number < 2:
    print("Not prime")
else:
    Prime = True

    for i in range(2, number):
        if number % i == 0:
            Prime = False
            break
    if Prime:
        print("Prime")
    else:
        print("Not prime")