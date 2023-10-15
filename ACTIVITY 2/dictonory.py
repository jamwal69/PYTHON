# Create a sample dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'country': 'USA'
}

# Using a for loop to iterate over the dictionary keys
print("Iterating over the dictionary keys using a for loop:")
for key in my_dict:
    print(key)

# Using a for loop to iterate over the dictionary values
print("\nIterating over the dictionary values using a for loop:")
for value in my_dict.values():
    print(value)

# Using a for loop to iterate over key-value pairs (items)
print("\nIterating over key-value pairs using a for loop:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Using a dictionary comprehension to create a new dictionary during iteration
print("\nIterating and filtering dictionary items using dictionary comprehension:")
filtered_dict = {key: value for key, value in my_dict.items() if key != 'country'}
print(filtered_dict)
