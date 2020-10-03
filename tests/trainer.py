def is_palindrome(word):
    new_word = str(word).upper()
    return new_word[::-1] == new_word

def test_is_palindrome_empty_string():
    assert is_palindrome("")

def test_is_palindrome_single_character():
    assert is_palindrome("a")

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")

def test_is_polindrome_not_palindrome():
    assert not is_palindrome("abc")

def test_is_palindrome_with_spaces():
    assert is_palindrome("is si")

def test_is_palindrome_with_symbols():
    assert is_palindrome("!ii!")

def test_is_palindrome_with_numbers():
    assert is_palindrome(121)
