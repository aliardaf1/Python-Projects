from fuel import convert , gauge
import pytest

def main():
    test1()
    test2()

def test1():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")
def test2():
    assert convert("1/2") == 50
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
if __name__ == "__main__" :
    main()