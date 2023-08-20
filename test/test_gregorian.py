from main import gregorian

def test_leap_year():
    year = 1992
    leap = gregorian.calendar(year)
    expected = True
    assert leap == expected