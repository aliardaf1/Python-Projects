from um import count

def main():
    test_upper_lower_case()
    test_word_with_um()
    test_space()

def test_upper_lower_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, oh, um..") == 2
def test_word_with_um():
    assert count("Number of people") == 0
    assert count("You are, um, dumb!") == 1
def test_space():
    assert count(" um ") == 1


if __name__ == "__main__":
    main()