from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten('casa.') == 'cs.'
    assert shorten('camelo') == 'cml'


if __name__ == '__main__':
    main()