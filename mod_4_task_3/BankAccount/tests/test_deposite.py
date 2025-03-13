from mod_4_task_3.BankAccount.BankAccount import BankAccount
import pytest

@pytest.mark.parametrize('data, expected',[
    (11,11),
    (11.1,11.1),
    (788,788),
    (123454321, 123454321),
    (12345321, 12345321)
])

def test_positive(data,expected):
    b = BankAccount()
    b.deposit(data)
    assert b.get_balance() == expected


@pytest.mark.parametrize('data, expected',[
    (0,0)
])

def test_bound(data,expected):
    b = BankAccount()
    b.deposit(data)
    assert b.get_balance() == expected


@pytest.mark.parametrize('data, expected',[
    (-1, ValueError),
    ('3.13', TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        b = BankAccount()
        b.deposit(data)
        b.get_balance()