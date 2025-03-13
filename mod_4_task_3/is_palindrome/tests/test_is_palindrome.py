from mod_4_task_3.is_palindrome.is_palindrome import is_palindrome
import pytest

@pytest.mark.parametrize('data, expected',[
    ('111',True),
    ('787',True),
    ('788',False),
    ('123454321', True),
    ('12345321', False)
])

def test_positive(data,expected):
    assert is_palindrome(data) == expected


@pytest.mark.parametrize('data, expected',[
    ('1',True),
    ('',False),
    ('Pop', False)
])

def test_bound(data,expected):
    assert is_palindrome(data) == expected


@pytest.mark.parametrize('data, expected',[
    (11, TypeError),
    (3.13, TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        is_palindrome(data)