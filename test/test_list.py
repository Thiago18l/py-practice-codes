from main import list_comprehensions
import pytest

@pytest.mark.parametrize("input_values, expected_output", [
    ((1, 1, 1, 2), "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n")
])
def test_calculate_coordinates(input_values, expected_output, capsys):
    x, y, z, n = input_values
    list_comprehensions._list(x, y, z, n)
    captured = capsys.readouterr()
    assert captured.out == expected_output
