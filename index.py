my_list = []
my_list.append(10) 
my_list.append(20)
my_list.append(30)
my_list.append(40)

print  ("Appended List")
print(my_list)

print("Extended List")
my_list.extend([50, 60, 70])
print(my_list)

print("Removing the last Number")
my_list.remove(70)
print(my_list)

print("find 30")
number = 30

try:
    index = my_list.index(number)
    print(f"{number} found at index {index}.")
except ValueError:
    print(f"{number} is not in the list.")
    
print (" Sorting number")
my_list.sort()
print(my_list)
