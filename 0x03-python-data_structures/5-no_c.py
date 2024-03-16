#!/usr/bin/python3

def no_c(my_string):
    # Create an empty string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is 'c' or 'C'
        if char != 'c' and char != 'C':
            # If not, append it to the result string
            result += char
            
    # Return the resulting string
    return result
