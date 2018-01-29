my_list = ["Chandrakanth", "dandamoodi", "third", "fourth", "fifth"]

# ["Chandrakanth", "dandamoodi", "third"]
#     0, 1, 2
#     -3, -2, -1
# Below two point to the same value
print(my_list[0])
print(my_list[-3])

# Replace a value in a list
my_list[1] = "second"
print(my_list)

# Check if avalue is present in list
print("Chandrakanth" in my_list)

# Size of list
print(len(my_list))

# Remove a element from the list
del my_list[2]
print(my_list)

# get sublist
print(my_list[1:])

# get all except first and last element
print(my_list[1:-1])