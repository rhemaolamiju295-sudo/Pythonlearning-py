#Lists
    # list are used to store multiple items in a single variable. it is an inbuilt data types in python the other three data types are: Tuple, Set and Dictionary

my_list = ["Apple", "Banana", "Cherry", "Pear", "Watermelon"]
if "Pear" in my_list:
    print("Yes, pear is in the list")
print(my_list)

#aList can be sliced, lists can also be indexed 
#Accessing List items
print(my_list[0]) #This indexing/slicing of list it prints the first string in the list
print(my_list[-1]) #This prints the last string in the string 
print(my_list[1])
print(my_list[2:5]) # Rang indexing return from the 3rd item to the 5th item
print(my_list[:4]) # returns every item from the begining and stop at the 4th item
print(my_list[2:])
print(my_list[-4:-2]) # negative index ranging 


#The length of a list can also be printeed:
print(len(my_list))
print(type(my_list))

# Lists are classified into the data type calles LIST
# list can basically contain different data type: int, bool, string e.c.t
this_list = ["abc", 34, True, 40, "Male"]
print(this_list)

list1 = list(("apple", "banana", "cherry"))
if "cherry" in list1:
    print("yes")
print(list1)

#checking if item is in list 
if "Watermelon" in my_list:
    print("yes")

#Changing the values of items in a list

my_list[2] = "buleberry"
print(my_list)

my_list[0:2] = "happey-hour", "Mr.Fruits" #changing range of item values 
print(my_list)

my_list[1:3] = ["Watermelon"]
print(my_list)

#Inserting items
    # To insert a new list item, without replacing any of the existing values, we can use the insert() method.

list1.insert(2, "YCCE") #the number is indicating that the inserted item should be instered index number 2 
print(list1) 

#Append Items
    #To add an item to the end of the list, use the append() method:

list1.append("Tony-Enumelu")
print(list1)
#Extend list
    #To append elements from another list to the current list, use the extend() method.
list1.extend(my_list)
print(list1)

#Remove specified item
    #The remove() method removes the specified item.

list1.remove("banana")
print(list1)
 #WHAT IF you want to remove a specified or specific index:
 #we use the pop method pop()
 #the keyword: del can also delete lists
thislist = ["agbado", "pawpaw", "yam"]
del thislist[0]
print(thislist)

list1.pop(1)
print(list1)

list1.pop() #If you do not specify the index, the pop() method removes the last item.
print(list1)
# The clear() method empties the list.
# The list still remains, but it has no content.

thislist.clear()
print(thislist)

#sorting and reversing lists

numbers = [8, 5, 2, 1, 3, 4, 9]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

sotered_numbers = sorted(numbers)
print(sotered_numbers)


a = [1, 2, 3]
b = a
b.append(4)
print(a)

c = a.copy()
c.append(5)
print(a)
print(c)

#Nested list 

mixed = ["Bolu", 21, True, 3.14]
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[0])       # [1, 2]
print(nested[2][1])    # 2 — access an item inside the inner list


#nOTE:
# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.
