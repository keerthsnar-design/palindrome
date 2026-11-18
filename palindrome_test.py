from palindrome import is_palindrome

def test_palindrome():
    assert is_palindrome("madam") == True

def test_not_palindrome():
    assert is_palindrome("hello") == False

def test_uppercase():
    assert is_palindrome("MADAM") == True

def test_number():
    assert is_palindrome("121") == True