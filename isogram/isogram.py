def is_isogram(string):
    chars = set()
    string = string.lower()

    for char in string:
        if char in chars and char not in ' -':
            return False
        chars.add(char)

    return True
