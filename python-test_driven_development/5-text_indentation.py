#!/usr/bin/python3
"""Module containing text_indentation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ?, and :."""
    
    # Check if text is a string
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    # Iterate through the text and print with proper newlines
    i = 0
    while i < len(text):
        # Print the current character
        print(text[i], end="")
        
        # If the character is one of '.', '?', or ':', add two new lines
        if text[i] in ['.', '?', ':']:
            print("\n")
        
        i += 1
