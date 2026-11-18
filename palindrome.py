def is_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        return f"{string} is a Palindrome"
    else:
        return f"{string} is not a Palindrome"