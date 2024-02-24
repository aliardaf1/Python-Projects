from numb3rs import validate

def main():
    test_validate_format()
    test_validate_digit()
    test_validate_range()

def test_validate_format():
    assert validate(r"1.2.3") == False
    assert validate(r"1.55") == False
    assert validate(r"1.2.4.5") == True

def test_validate_digit():
    assert validate(r"cat.cat.cat.cat") == False

def test_validate_range():
    assert validate(r"-2.3.34.5") == False
    assert validate(r"25.23.2.256") == False
    assert validate(r"5.2587.-2.3") == False

if __name__ == "__main__" :
    main()