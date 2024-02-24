from bank import value

def main():
    test_h()
    test_hello()
    test_non()

def test_h():
    assert value("h me son") == 20
    assert value("hi dude") == 20
def test_hello():
    assert value("hello dude") == 0
    assert value("Hello") == 0
def test_non():
    assert value("give me give me") == 100
    assert value("  sss") == 100

if __name__ == "__main__":
    main()