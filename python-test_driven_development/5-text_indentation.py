#!/usr/bin/python3
"""Module containing text_indentation function"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.
    The function ensures there is no leading or trailing space on each printed line.

    Args:
        text: The input string to be processed.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # We want to iterate through the text and print lines based on characters ., ?, :
    # Use a flag to help with spacing control after each of these characters
    delimiters = ['.', '?', ':']
    temp_line = ""

    for char in text:
        if char in delimiters:
            # Append the current character to the temporary line and print it
            temp_line += char
            print(temp_line.strip())
            print()  # Newline after each of these characters
            temp_line = ""  # Reset the temporary line
        else:
            # If not a delimiter, add the character to the temporary line
            temp_line += char

    # Finally, print any remaining text in temp_line (if any)
    if temp_line:
        print(temp_line.strip())
