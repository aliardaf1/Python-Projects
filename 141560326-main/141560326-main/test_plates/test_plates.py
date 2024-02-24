from plates import is_valid

def main():
    test_is_valid_length()
    test_is_valid_punct()
    test_is_valid_begin()
    test_is_valid_0()

def test_is_valid_length():
    assert is_valid("ASDSADADS") == False
    assert is_valid("s") == False

def test_is_valid_punct():
    assert is_valid("AB223,") == False

def test_is_valid_begin():
    assert is_valid("12ABSE") == False
    assert is_valid("AB223A") == False
    assert is_valid("223") == False

def test_is_valid_0():
    assert is_valid("AA230A2") == False
    assert is_valid("AA023") == False

if __name__ == "__main__" :
    main()