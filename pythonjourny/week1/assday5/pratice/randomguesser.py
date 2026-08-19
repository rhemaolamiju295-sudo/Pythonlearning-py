import random 

secrete = random.randint(1, 100)
print(secrete)

attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess == secrete: 
        print(f"Correct it took you {attempts} attempts")
        break  
    elif guess < secrete:
        print("Too low")
    else:
        print("Too high")

