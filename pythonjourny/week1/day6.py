#Lists
    # list are used to store multiple items in a single variable. it is an inbuilt data types in python the other three data types are: Tuple, Set and Dictionary

my_list = ["Apple", "Banana", "Cherry", "Pear", "Watermelon"]
print(my_list)

#aList can be sliced, lists can also be indexed 
#Accessing List items
print(my_list[0]) #This indexing/slicing of list it prints the first string in the list
print(my_list[-1]) #This prints the last string in the string 
print(my_list[1])
print(my_list[2:5]) # Rang indexing return from the 3rd item to the 5th item
print(my_list[:4]) # returns every item from the begining and stop at the 4th item
print(my_list[2:])
print(my_list[-4:-2])


#The length of a list can also be printeed:
print(len(my_list))
print(type(my_list))

# Lists are classified into the data type calles LIST
# list can basically contain different data type: int, bool, string e.c.t
this_list = ["abc", 34, True, 40, "Male"]
print(this_list)

list1 = list(("apple", "banana", "cherry"))
print(list1)




# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.
