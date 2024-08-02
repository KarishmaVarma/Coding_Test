#2. Write a Python function to reverse a string.	
def reverse_string(s):
    return s[::-1]  # Use slicing to reverse the string

original_string = "Hello, World!"
reversed_string = reverse_string(original_string)

# Print the original and reversed strings
print("Original string:", original_string)
print("Reversed string:", reversed_string)

#Output:
"""
Original string: Hello, World!
Reversed string: !dlroW ,olleH
"""
