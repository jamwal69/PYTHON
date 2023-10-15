# Create a sample list
my_list = [1, 2, 3, 4, 5]

# Using a for loop to iterate over the list
print("Iterating over the list using a for loop:")
for item in my_list:
    print(item)

# Using a while loop to iterate over the list
print("\nIterating over the list using a while loop:")
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# Using enumerate to get both index and value during iteration
print("\nIterating over the list with index and value using enumerate:")
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# Using a list comprehension to iterate and manipulate the list
print("\nIterating and squaring each element using list comprehension:")
squared_list = [x ** 2 for x in my_list]
print(squared_list)
