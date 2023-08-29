# Define a function named highest_consonant_value that takes a single argument: string
def highest_consonant_value(string):
    vowels = set("aeiou")  # Create a set containing the vowel characters
    max_value = 0  # Initialize a variable to store the highest consonant value

    # Iterate through each character in the input string
    for char in string:
        if char not in vowels:  # Check if the character is not a vowel
            # Calculate the value of the consonant (its position in the alphabet)
            value = ord(char) - ord('a') + 1
            if value > max_value:  # Check if the current value is greater than the stored max value
                max_value = value  # Update the max_value if the current value is larger

    # Return the highest consonant value found in the string
    return max_value

# Example usage
result = highest_consonant_value("hello world")
print(result)  # Output will be 18, as 'h' has the highest consonant value
