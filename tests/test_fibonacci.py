import pytest
import fibonacci


@pytest.mark.parametrize("number, expected", [(1, [0]), (4, [0, 1, 1, 2]), (7, [0, 1, 1, 2, 3, 5, 8])])
def test_fibonacci(number, expected):
    assert list(fibonacci.generateFibonacci(number)) == expected