age = 21

if age >= 18:
    print("eligible")

else:
    print("Not eligible")


message = "Pikin" if age >= 18 else "Agba"
print(message)

i_get_babe = False
i_get_crush = False

if i_get_babe == False and i_get_crush == True:
    print("Senior man")
else:
    print("You are single bro" )


score = 100

my_list = ["Apples", "Oranges", "Mangoes", "Bananas"]

my_list.append("Watermelon")
my_list.insert(2, "Avocado")
my_list.insert(4, "Pineapple")

my_list.remove("Avocado")
my_list.pop(1)

for i in range(len(my_list)):
    print(my_list[i])
print(my_list)


number = 20

if number > 0:
    print("Positive number")

a = 40 
b = 40

if b > a:
    print("b is greater than a")
elif b == a:
    print("Both a and b are equal")


age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenagre")
else:
    print("Adult")


age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Need ID")
else:
    print("Too young")

for i in range(5):
  print("hello")
