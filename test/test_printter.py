from main import printter

def test_printter():
    expected: list = [1, 2, 3]
    result = printter.printter(3)
    
    assert expected == result