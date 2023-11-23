def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

def is_armstrong(number):
    # Function to calculate the sum of cubes of each digit in the number
    def sum_of_cubes(num):
        return sum(int(digit) ** 3 for digit in str(num))

    # Check if the number is equal to the sum of cubes of its digits
    return number == sum_of_cubes(number)

# Example usage of max_of_three
result_max = max_of_three(10, 5, 8)
print(f"The largest of the three numbers is: {result_max}")

# Example usage of is_armstrong
num_to_check = 153
if is_armstrong(num_to_check):
    print(f"{num_to_check} is an Armstrong number.")
else:
    print(f"{num_to_check} is not an Armstrong number.")
