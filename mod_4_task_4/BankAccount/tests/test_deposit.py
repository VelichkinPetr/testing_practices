import pytest
from mod_4_task_4.BankAccount.BankAccount import BankAccount


@pytest.fixture(scope= 'function')
def bank_account():
    data = BankAccount()
    return data


@pytest.mark.ba
@pytest.mark.parametrize('data, expected',[
    (11,11),
    (11.1,11.1),
    (788,788),
    (123454321, 123454321),
    (12345321, 12345321)
])

def test_positive(bank_account,data,expected):
    assert bank_account.deposit(data) == expected

@pytest.mark.ba
@pytest.mark.parametrize('data, expected',[
    (0,0)
])

def test_bound(bank_account, data,expected):
    assert bank_account.deposit(data) == expected

@pytest.mark.ba
@pytest.mark.parametrize('data, expected',[
    (-1, ValueError),
    ('3.13', TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(bank_account, data,expected):
    with pytest.raises(expected):
        bank_account.deposit(data)
