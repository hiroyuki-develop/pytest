import pytest
from src.calc import add, evenodd

def test_add():
    assert add(2, 3) == 5
    assert add(1, 1) == 2

@pytest.mark.parametrize(("num", "expected"),
    [
        (1,  "奇数"),
        (2,  "偶数"),
        (3,  "奇数"),
        (4,  "偶数"),
        (5,  "奇数"),
        (6,  "偶数"),
        (7,  "奇数"),
        (8,  "偶数"),
        (9,  "奇数"),
        (10, "偶数"),
    ]
)
def test_evenodd(num, expected):
    assert evenodd(num) == expected