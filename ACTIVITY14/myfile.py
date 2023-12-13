def create_and_write_file(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def main():
    file_path = "MyFile.txt"
    user_lines = []

    # Ask the user to input three lines
    for i in range(3):
        user_input = input(f"Enter line {i + 1}: ")
        user_lines.append(user_input)

    # Create and write the lines to the file
    create_and_write_file(file_path, user_lines)
    print(f"File '{file_path}' has been created with the user's input.")

if __name__ == "__main__":
    main()
