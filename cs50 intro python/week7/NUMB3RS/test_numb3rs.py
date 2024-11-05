from numb3rs import validate

def main():
    test_max()
    test_min()
    test_nm()
    test_rand()



def test_max():
    assert validate("255.255.255.255") == True
    assert validate(".255.255.255.255") == False
    assert validate("55.255.255.255f") == False

def test_min():
    assert validate("0.0.0.0") == True
    assert validate(".0.0..00.") == False
    assert validate("0.30d.0.0") == False

def test_nm():
    assert validate("123.123.123.123") == True

def test_rand():
    assert validate("cat") == False
    assert validate("265.424.326.y543") == False


if __name__ == '__main__':
    main()