def highest_consonant_value(string):
    vowels = set("aeiou")
    max_value = 0

    for char in string:
        if char not in vowels:
            value = ord(char) - ord('a') + 1
            if value > max_value:
                max_value = value

    return max_value
