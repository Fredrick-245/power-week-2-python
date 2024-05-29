# Create an empty list
my_list=[]

# Append 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 in the second last position
my_list.insert(len(my_list)-1,15)

# Extend the list with [50,60,70]
my_list.extend([50,60,70])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of 30 and print it
index_of_val = my_list.index(30)
print(index_of_val)