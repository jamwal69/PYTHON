def demonstrate_type_checking_and_builtin_functions(data):
    # Type checking using the 'type()' function
    data_type = type(data)
    print(f"Data Type: {data_type}")

    if data_type == int:
        # Demonstrating the 'abs()' function for integers
        absolute_value = abs(data)
        print(f"Absolute Value: {absolute_value}")

    if data_type in (str, list, tuple, dict):
        # Demonstrating the 'len()' function for strings, lists, tuples, and dictionaries
        length = len(data)
        print(f"Length: {length}")

    if data_type in (int, float):
        # Demonstrating the 'round()' function for integers and floats
        rounded_value = round(data, 2)
        print(f"Rounded Value (to 2 decimal places): {rounded_value}")

    if data_type == str:
        # Demonstrating the 'isalnum()' function for strings
        is_alphanumeric = data.isalnum()
        print(f"Is Alphanumeric: {is_alphanumeric}")

    if data_type in (list, tuple):
        # Demonstrating the 'min()' function for lists and tuples
        if len(data) > 0:
            minimum_value = min(data)
            print(f"Minimum Value: {minimum_value}")
        else:
            print("List or tuple is empty.")

# Test cases with various data types
demonstrate_type_checking_and_builtin_functions(42)  # Integer
demonstrate_type_checking_and_builtin_functions("Hello123")  # String
demonstrate_type_checking_and_builtin_functions([3, 1, 4, 1, 5, 9])  # List
demonstrate_type_checking_and_builtin_functions((3.14, 2.71, 1.62))  # Tuple
demonstrate_type_checking_and_builtin_functions(3.14159)  # Float
demonstrate_type_checking_and_builtin_functions({"name": "John", "age": 30})  # Dictionary
