# ------------------------- #
# -- Decorators => Intro -- #
# ------------------------- #
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ------------------------------------------------------------------------------


# Function to print a pattern of stars
def stars(n, dir=True, startPoint=0):
    """
    Print a pyramid pattern of stars.

    Args:
    n (int): The maximum width of the star pattern.
    dir (bool): Direction of the pattern; True for decreasing width, False for increasing width.
    startPoint (int): Offset for centering the pattern.

    The function adjusts the spaces and prints stars in either a decreasing or increasing pattern based on 'dir'.
    """
    if dir:  # For decreasing pattern
        for i in range(n, 0, -2):  # Start from 'n' and decrement by 2
            spaces = max(
                startPoint - n // 2, 0
            )  # Calculate spaces to align the pattern
            print(
                " " * ((n - i) // 2 + spaces) + "*" * i
            )  # Print spaces followed by stars
    else:  # For increasing pattern
        for i in range(1, n + 1, 2):  # Start from 1 and increment by 2
            spaces = max(
                startPoint - n // 2, 0
            )  # Calculate spaces to align the pattern
            print(
                " " * ((n - i) // 2 + spaces) + "*" * i
            )  # Print spaces followed by stars


# A decorator function to enhance another function
def myFirstDecorator(func):
    """
    A decorator that prints a star pattern before and after the output of the decorated function.

    Args:
    func (function): The function to be decorated.

    Returns:
    function: The decorated function with star patterns around its output.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Call the original function and get its result
        result_len = len(result)  # Calculate the length of the result string
        centered_offset = (
            result_len // 2
        )  # Determine offset for centering the star pattern

        stars(7, startPoint=centered_offset)  # Print a star pattern above the result
        print(func(*args, **kwargs))  # Print the result of the decorated function
        stars(
            7, False, startPoint=centered_offset
        )  # Print a star pattern below the result

    return wrapper  # Return the wrapped function


# Function to calculate the sum of two numbers, decorated with myFirstDecorator
@myFirstDecorator
def sum(n1, n2):
    """
    Calculate the sum of two numbers and return a formatted string.

    Args:
    n1 (int): The first number.
    n2 (int): The second number.

    Returns:
    str: A formatted string displaying the sum of the numbers.
    """
    return f"The Sum of {n1} + {n2} = {n1 + n2}"


# Function to greet a user by name, decorated with myFirstDecorator
@myFirstDecorator
def sayHello(name):
    """
    Return a greeting message.

    Args:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello {name} from SayHello Func"


# Call the decorated 'sum' function with arguments 5 and 7
sum(5, 7)
print("-" * 40)  # Print a separator line
# Call the decorated 'sayHello' function with the name "Kareem"
sayHello("Kareem")
