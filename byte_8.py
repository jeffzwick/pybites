def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    new_string = string[n:] + string[:n]
    return new_string


print(rotate("hello", 2))
print(rotate("hello", -2))