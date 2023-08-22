from main import score
import pytest

@pytest.mark.parametrize("n, arr, expected_runner_up", [
    (5, [2, 3, 6, 6, 5], 5),
    (6, [1, 1, 1, 1, 1, 1], None),
    (4, [9, 8, 7, 7], 8),
])
def test_score_func(n, arr, expected_runner_up):
    assert score.score_(n, arr) == expected_runner_up