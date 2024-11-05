from working import convert

def test_convert_1():
    assert convert("9 AM to 15 PM") == "09:00 to 15:00"

def test_convert_2():
    assert convert("10:30 AM to 3:30 PM") == "10:30 to 15:30"

def test_convert_3():
    assert convert("1 AM to 5 PM") == "01:00 to 17:00"

