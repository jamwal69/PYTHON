#a) Count the number of alphabets in the given string.

string = "Welcome to Python world"
alphabet_count = sum(1 for char in string if char.isalpha())
print("Number of alphabets in the string:", alphabet_count)

#b) To extract characters in the given, range from the given string. 
string = "Welcome to Python world"
start_index = 8
end_index = 13
substring = string[start_index:end_index+1]
print("Extracted substring:", substring)

#c) Check if the string is alphanumeric or not.
string = "Welcome to Python world"
is_alphanumeric = string.isalnum()
if is_alphanumeric:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")
