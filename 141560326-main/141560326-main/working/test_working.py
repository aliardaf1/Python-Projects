from working import convert
import pytest

def main():
    test_format()
    test_time()
    test_wrong_hour()
    test_wrong_minute()

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 11 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 15 PM")

def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 11:60 PM")

if __name__ == "__main__" :
    main()