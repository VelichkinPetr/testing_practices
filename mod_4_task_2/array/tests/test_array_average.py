from mod_4_task_2.array.array import Array
import pytest

@pytest.mark.parametrize('data, expected',[
    ((1,2,3),2),
    ((-1,2,3,0),1),
    ((-1,-2,-3),-2),
    ((-1,-2,3),0),
    ((3,5,10),6)
])

def test_positive(data,expected):
    assert Array(*data).average() == expected


@pytest.mark.parametrize('data, expected',[
    ((1,-1),0),
    ((0,0),0),
    ([0],0),
    ([111],111)
])

def test_bound(data,expected):
    assert Array(*data).average() == expected


@pytest.mark.parametrize('data, expected',[
    (('', 1), TypeError),
    ((22, [55]), TypeError),
    (('0', 0), TypeError),
    (('0', '0'), TypeError),
    (([], []), TypeError),
    ((None, 1), TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        Array(*data).average()