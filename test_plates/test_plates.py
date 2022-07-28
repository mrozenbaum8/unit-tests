from plates import is_valid

def main():
    test_isvalid()
    test2_isvalid()
    test3_isvalid()
    test4_isvalid()
    return 0


def test_isvalid():
    assert is_valid('CS50') == True

def test2_isvalid():
    assert is_valid('CS05') == False
    assert is_valid('!S0C') == False

def test3_isvalid():
    assert is_valid('CS50P') == False
    assert is_valid('1S50') == False
    assert is_valid('C') == False
    assert is_valid('9868') == False

def test4_isvalid():
    assert is_valid('PI3.14') == False



if __name__ == "__main__":
    main()