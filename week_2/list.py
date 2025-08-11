# 📘 Assignment: Working with Python Lists

# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append elements to the list
# We're adding four numbers one by one using the append() method
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert the value 15 at the second position (index 1)
# The list will now be: [10, 15, 20, 30, 40]
my_list.insert(1, 15)

# Step 4: Extend my_list with another list [50, 60, 70]
# This adds all the elements of the new list to the end of my_list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from my_list
# pop() with no argument removes the last item (70 in this case)
my_list.pop()

# Step 6: Sort the list in ascending order
# This rearranges the list from the smallest to the largest value
my_list.sort()

# Step 7: Find and print the index of the value 30
# index() returns the position of the first occurrence of the value
index_of_30 = my_list.index(30)

# Print the final list and the index of 30
print("📝 Final List:", my_list)
print("📍 Index of 30:", index_of_30)
