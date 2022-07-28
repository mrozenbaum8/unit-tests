from bank import value

def main():
    test_value()
    return 0


def test_letter():
    assert value('K') == 100

def test_word():
    assert value('Test') == 100
    assert value("Hello") == 0
    assert value('Hi') == 20

def test_number():
    assert value('5') == 100

if __name__ == "__main__":
    main()