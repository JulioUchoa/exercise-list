from bank import value

def main():
    test_value_start_hello()
    test_value_start_h()
    test_value_other()


def test_value_start_hello():
    assert value("Hello, world") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_value_start_h():
    assert value("hi there!") == 20
    assert value("Howdyoudoing") == 20
    assert value("Hoorait!") == 20

def test_value_other():
    assert value("Good Morning!") == 100
    assert value("412632") == 100
    assert value("Julio is here") == 100


if __name__ == '__main__':
    main()