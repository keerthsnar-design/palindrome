from palindrome import is_palindrome

def test_palindrome_positive():
    result = is_palindrome("madam")
    assert result == "madam is a Palindrome"

def test_palindrome_negative():
    result = is_palindrome("hello")
    assert result == "hello is not a Palindrome"