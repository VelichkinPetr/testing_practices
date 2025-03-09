from mod_4_task_2.calculator.calculator import Calculator
import pytest

@pytest.mark.parametrize('value_left, value_right, expected',[
    (10,1,10),
    (11,11,121),
    (-11,11,-121),
    (-2,0,0)
])

def test_positive(value_left, value_right,expected):
    assert Calculator().multiply(value_left,value_right) == expected


@pytest.mark.parametrize('value_left, value_right, expected',[
    (-1,-1,1),
    (0,0,0)
])

def test_bound(value_left, value_right,expected):
    assert Calculator().multiply(value_left,value_right) == expected


@pytest.mark.parametrize('value_left, value_right, expected',[
    ('1',1,TypeError),
    (22,[55],TypeError),
    ('0',0,TypeError),
    (None,1,TypeError)
])

def test_negative(value_left, value_right,expected):
    with pytest.raises(expected):
        Calculator().multiply(value_left,value_right)