day3 = "Strings deepdive"
print(len(day3))

alphabets = "abcdefghijklmnopqrstuvwxyz"
#basically all these are used to slice strings in other words string slicer 
print(alphabets[-1]) #Negative number can also slice to the end charcter of the string   
print(alphabets[0]) #python starts a count frm 0 e.g the word "python" would be counted as "012345"
word = "python"
print(word[::2])
print(word[::-1])

print(alphabets[0:3]) #Toice between range of the string determining what part of the length of the string should be printed 

# in today's lesson i dont have a not book with me so ill be documenting note in my code for referencing 

#escape cases: these are escape sequences written with a backslash(\) inside strings. 
#Types are: 1. Adding qoutes(double/single) inside a string: e.g "python \"programming"" 
#           2. New line : e.g "Hello \nWorld" e.t.c

print("python programming")
print("python\"programming\"")
print("python \nprogramming")
print("\\python\\progranning")

#Formatted strings: tis uses concatination(joining two variables together)
first_name = input("input your first name: ")
last_name = input("input your last name: ")
fullname = first_name + " " + last_name
print(fullname)

#String method: Mothod are functions attached to a string using dot notation 

text = " Bolu Dev "
text.upper()
print(text)
