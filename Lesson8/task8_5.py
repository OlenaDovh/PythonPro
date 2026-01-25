import pytest


def divide(a: int, b: int) -> float:
    """Returns the result of dividing two numbers"""
    if b == 0:
        raise ZeroDivisionError("Division by 0 is prohibited")
    return a / b


testdata = [
    (4, 2, 2.0),
    (15, 6, 2.5),
    (10.2, 2, 5.1),
    (-8, 16.2, -0.4938271604938272)
]


@pytest.mark.parametrize("a, b, expect_res", testdata)
def test_divide_with_diff_values(a, b, expect_res):
    assert divide(a, b) == expect_res


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(7, 0)
