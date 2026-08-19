#While loops
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)


a = 0

while a < 6:
    a += 1
    if a == 3:
        continue # it is used to stop the current iteration of the loop and continue with the next 
    print(a)

#For loops
bills = ["Tithes", "Opay-bills", "Feeding", "Trnsportation"]
for y in bills:
    print(y, end=" ")
    if y == "Feeding":
        break 
print()

fruits = ["cherry", "banana", "apple"]
for x in fruits[:2]: # this prints the first two inputs of the fruit variable  
    print(x)
# ranges is used to loop through a set of code of a variable a specific number of times 
for g in range(6): #range function starting default is from 0 so it counts from zero 
    print(g)

for h in range(2, 6):# but we can always assign a value for it to start counting from instead of the default 0 
    print(h)
for x in range(2, 1102, 2):# we can also add an increment to the value to increase count 
     print(x, end=" ")# THe (end=" ") is used to print the outputs on a horizontal line instead of printing the output on a vertical or straight line  
else:
     print() # This print a new line after the output 
     print("Jut finished writing even nuumbers")





transport = 1600 

n = transport * 20

print(n)

transport = 32000
tithes = 10000
feeding = 30000
youth = 8000
opay = 5200
pledge = 10000
pebbles = 100000
n = (transport + tithes + feeding + youth + opay + pledge)

pebbles = pebbles - n
print(n)
print(pebbles)


def solution(name, cohort):
    return f"Name: {name}\nCohort: {cohort}\nStatus: Ready"

print(solution("Volu", "Cohort1"))

for letter in "python" :
    print(len("python"))

for b in range(1, 20):
    if b % 2 == 0:
        continue
    print(b, end = " ")
print()

#Nested Loops: A loop inside a loop- common for grids, tables nd patters 

for c in range(3):
    for d in range(3):
        print(f"i = {c}, y = {d})")

for e in bills:
    for f in fruits:
        print(e,  f, end = ", ")
print()

for index, bill in enumerate(bills):
    print(index, bill) 

print(len("Python"))