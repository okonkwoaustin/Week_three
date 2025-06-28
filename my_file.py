# Task: 3 Read File with Line Numbers


def read_files(filename):
    """
    Reads a file and prints each line with line numbers.

    Args:
        filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            for n, line in enumerate(file, start=1):
                print(f"{n}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found")


read_files('data.txt')

# Task 4: Append User Input to File


def append_to_file(filename):
    """
    Asks the user for input and appends it to a file.

    Args:
        filename (str): The name of the file to append to.
    """
    try:
        user_input = input("Please enter some text: ")
        with open(filename, 'a') as file:
            file.write(user_input + "\n")
        print(f"Text appended to '{filename}'")
    except FileNotFoundError:
        return(f"File {filename} not found")

append_to_file('data.txt')