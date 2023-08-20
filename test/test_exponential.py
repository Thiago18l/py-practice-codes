from main import exponential

def test_exponential():
    result = exponential(5)
    expected: list = [0, 1, 4, 9, 16]
    assert result == expected