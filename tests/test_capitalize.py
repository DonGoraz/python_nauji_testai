
def capitalize_letters(world):
    return world.upper()

def is_reverse(world):
    return world[::-1]

def is_palendrome(world):
    return str(world) == str(world)[::-1]
    # elif not world:
    #     return True
    # else:
    #     return False

def is_palendrome_not_number(world):
    try:
        float(world)
        return True
    except ValueError:
        return False


def test_capitalize_letters():
    assert capitalize_letters("world") == "WORLD"

def test_capitalize_letters_number():
    assert capitalize_letters(1) == "WORLD"

def test_is_reverse():
    assert is_reverse(123.321)

def test_is_palendrome():
    assert is_palendrome("asa")

def test_is_palendrome_not_number():
    assert is_palendrome_not_number(5)

def test_is_palendrome_empty_string():
    assert is_palendrome()
