from plates import is_valid

def main():
    test_is_valid_few()
    test_is_valid_ran()
    test_is_valid_many()
    test_is_valid_especial()


def test_is_valid_few():
    assert is_valid("H") == False
    assert is_valid("1") == False

def test_is_valid_many():
    assert is_valid("CS500000") == False
    assert is_valid("CSGFR50") == False

def test_is_valid_ran():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA22A") == False
    assert is_valid("2453H") == False
    assert is_valid("ABERSDWT") == False

def test_is_valid_especial():
    assert is_valid("$@!%") == False
    assert is_valid("A%0@5") == False

if __name__ == '__main__':
    main()