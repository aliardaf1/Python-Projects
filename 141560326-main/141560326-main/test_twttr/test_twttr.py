from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("AEIOUB23") == "B23"
    assert shorten("BCD2312412610000010AAA") == "BCD2312412610000010"
    assert shorten("aeiou") == ""
    assert shorten("aeiou,") == ","
    assert shorten("AaEeIiBb") == "Bb"

if __name__ == "__main__" :
    main()