from jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    jar = Jar(10)
    assert jar.capacity == 10

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == '🍪'

def test_deposit_fail():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(11)
    assert str(jar) == '🍪'

def test_withdraw_fail():
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(14)



# faltam 2