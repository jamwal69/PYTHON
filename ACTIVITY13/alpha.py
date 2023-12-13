def get_unique_words(file_path):
    unique_words = set()

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        # Split the text into words and add them to the set
        for line in file:
            words = line.split()
            unique_words.update(words)

    return sorted(unique_words)

def main():
    # Get the file path from the user
    file_path = input("Enter the path of the text file: ")

    try:
        # Get unique words and print them in alphabetical order
        unique_words = get_unique_words(file_path)
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
