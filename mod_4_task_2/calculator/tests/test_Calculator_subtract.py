from mod_4_task_2.calculator.calculator import Calculator
import pytest

@pytest.mark.parametrize('value_left, value_right, expected',[
    (10,1,9),
    (22,55,-33),
    (-1,5,-6),
    (-2,-5,3)
])

def test_positive(value_left, value_right,expected):
    assert Calculator().subtract(value_left,value_right) == expected


@pytest.mark.parametrize('value_left, value_right, expected',[
    (1,-1,2),
    (0,0,0)
])

def test_bound(value_left, value_right,expected):
    assert Calculator().subtract(value_left,value_right) == expected


@pytest.mark.parametrize('value_left, value_right, expected',[
    ('', 1, TypeError),
    (22, [55], TypeError),
    ('0', 0, TypeError),
    ('0', '0', TypeError),
    ([], [], TypeError),
    (None, 1, TypeError)
])

def test_negative(value_left, value_right,expected):
    with pytest.raises(expected):
        Calculator().subtract(value_left,value_right)