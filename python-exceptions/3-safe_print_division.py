#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b  # Attempt division
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        print("Inside result: {}".format(result))  # Print result inside the finally block
    return result  # Return the result