from seasons import Date

def test_conv():
    result = Date("1988-12-27")
    assert result.conv() == "Eighteen million, two hundred fourteen thousand, five hundred sixty minutes"
