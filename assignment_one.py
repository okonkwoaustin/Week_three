# Write a function to find the factorial of a number
# Write a function that checks if a number is prime (limit to the first 10 prime numbers 2, 3, 5, 7, 11, 13, 17, 19, 23, 29).
# Write a script that reads from a file and prints each line with line numbers
# Write a script that asks the user for input and appends it to a file

# Task 1: Factorial Function
def factorial(n):
    """
    Returns the factorial of a number.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int or str: The factorial of n or an error message.
    """
    try:
        # Ensure input is an integer
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")

        # Check for negative input
        if n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    except TypeError as e:
        return f"TypeError: {e}"
    except RecursionError:
        return "Error: Maximum recursion depth exceeded"
    except Exception as e:
        return f"Unexpected error: {e}"

print(factorial(7))         # Valid
print(factorial(-2))        # Negative number
print(factorial("seven"))   # Invalid type

print()
print()

# Task 2: Prime number function
def is_prime(n):
    """
    Checks if a number is one of the first 10 prime numbers.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if n is one of the first 10 prime numbers, False otherwise.
    
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is a negative integer.
    """
    first_10_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    try:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        return n in first_10_primes
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False
    
print(is_prime(6))
print(is_prime(-4))
print(is_prime(7))

# Task: 3 Read File with Line Numbers
def print_file_with_line_numbers(filename):
    """
    Reads a file and prints each line with line numbers.
    
    Args:
        filename (str): The name of the file to read.
    """
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, start=1):
                print(f"{i}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found")


print_file_with_line_numbers('data.txt')

# Task 4: Append User Input to File

def append_to_file(filename):
    """
    Asks the user for input and appends it to a file.
    
    Args:
        filename (str): The name of the file to append to.
    """
    user_input = input("Please enter some text: ")
    with open(filename, 'a') as file:
        file.write(user_input + "\n")
    print(f"Text appended to '{filename}'")


append_to_file('data.txt')