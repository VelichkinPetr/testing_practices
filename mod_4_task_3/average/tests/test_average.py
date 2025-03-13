from mod_4_task_3.average.average import average
import pytest

@pytest.mark.parametrize('data, expected',[
    ([1,2,3,4,5],3),
    ([2,2,2,2],2),
    ([33,55],44),
    ([1.5,2.5,1], 1.6666666666666667)
])

def test_positive(data,expected):
    assert average(data) == expected


@pytest.mark.parametrize('data, expected',[
    ([1],1),
    ([0,0,0,0],0),
    ([0],0)
])

def test_bound(data,expected):
    assert average(data) == expected


@pytest.mark.parametrize('data, expected',[
    (11, TypeError),
    (3.13, TypeError),
    (None, ValueError),
    ([], ValueError),
    ([''], TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        average(data)