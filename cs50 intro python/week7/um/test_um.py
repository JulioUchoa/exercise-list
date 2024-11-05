from um import count
import pytest

def main():
    test_count()


def test_count():
    assert count("um, hello, um world") == 2

def test_count1():
    assert count("um?") == 1

def test_count2():
    assert count("Um, thanks for the album") == 1

def test_count3():
    assert count("Um, thanks, um...") == 2

main()