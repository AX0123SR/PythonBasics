def remove_last_to_first(s):
    # Store the original string length
    original_length = len(s)

    # Loop until the length of the string becomes equal to the original length
    while len(s) != original_length:
        # Remove the last character from the string
        last_char = s[-1]
        s = s[:-1]
        print("l:"+s)
        # Add the last character to the beginning of the string
        s = last_char + s
        print(s)

    return s

# Test the function with an example string
original_string = "hello"
result = remove_last_to_first(original_string)
print("Original String:", original_string)
print("Resulting String:", result)