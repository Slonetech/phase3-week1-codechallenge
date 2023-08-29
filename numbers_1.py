# Define a function named check_positive_two that takes three arguments: a, b, and c
def check_positive_two(a, b, c):
    positive_count = 0  # Initialize a variable to count the number of positive values

    if a > 0:
        positive_count += 1  # Increment the count if 'a' is positive
    if b > 0:
        positive_count += 1  # Increment the count if 'b' is positive
    if c > 0:
        positive_count += 1  # Increment the count if 'c' is positive

    # Return True if the positive count is exactly 2, otherwise return False
    return positive_count == 2

# Call the check_positive_two function with arguments 1, 2, and -3
result = check_positive_two(1, 2, -3)

# Print the result of the function call
print(result)  # Output will be False since only 1 and 2 are positive
