from mod_4_task_3.BankAccount.BankAccount import BankAccount
import pytest

@pytest.mark.parametrize('data, expected',[
    (11,89),
    (11.1,88.9),
    (2,98)
])

def test_positive(data,expected):
    b = BankAccount()
    b.deposit(100)
    b.withdraw(data)
    assert b.get_balance() == expected


@pytest.mark.parametrize('data, expected',[
    (0,100),
    (100,0),
    (99,1),
    (1,99),
    (-1,101)
])

def test_bound(data,expected):
    b = BankAccount()
    b.deposit(100)
    b.withdraw(data)
    assert b.get_balance() == expected


@pytest.mark.parametrize('data, expected',[
    (101, ValueError),
    ('3.13', TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(data,expected):
    with pytest.raises(expected):
        b = BankAccount()
        b.deposit(100)
        b.withdraw(data)
        b.get_balance()