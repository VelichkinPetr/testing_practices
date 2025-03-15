import os

import pytest
from mod_4_task_4.DiscountCalculator.DiscountCalculator import DiscountCalculator


@pytest.fixture(scope= 'function')
def discount_calculator():
    return DiscountCalculator()

@pytest.mark.dc
@pytest.mark.parametrize('data, expected',[
    ((100,30),70),
    ((333,33.3),222.11),
    ((500,20),400),
    ((33.3,33.3),22.21),
    ((1809,13),1573.83)
])

def test_positive(discount_calculator,data,expected):
    assert discount_calculator.apply_discount(*data) == expected

@pytest.mark.dc
@pytest.mark.parametrize('data, expected',[
    ((0, 30), 0),
    ((100, 0), 100),
    ((0.1, 20), 0.08),
    ((100,100),0)
])

def test_bound(discount_calculator, data,expected):
    assert discount_calculator.apply_discount(*data) == expected

@pytest.mark.dc
@pytest.mark.parametrize('data, expected',[
    ((-1,30), ValueError),
    ((3.13,-1), ValueError),
    ((20,110),ValueError),
    ((None,None), TypeError),
    (([121],20), TypeError),
    (([],10), TypeError)
])

def test_negative(discount_calculator, data,expected):
    with pytest.raises(expected):
        discount_calculator.apply_discount(*data)