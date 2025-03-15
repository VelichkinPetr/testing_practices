import pytest
from mod_4_task_4.BankAccount.BankAccount import BankAccount

@pytest.fixture(scope= 'function')
def bank_account():
    data = BankAccount()
    data.deposit(100)
    return data


@pytest.mark.ba
@pytest.mark.parametrize('data, expected',[
    (11,89),
    (11.1,88.9),
    (2,98)
])

def test_positive(bank_account,data,expected):
    assert bank_account.withdraw(data) == expected


@pytest.mark.ba
@pytest.mark.parametrize('data, expected',[
    (0,100),
    (100,0),
    (99,1),
    (1,99),
    (-1,101)
])

def test_bound(bank_account, data,expected):
    assert bank_account.withdraw(data) == expected


@pytest.mark.ba
@pytest.mark.parametrize('data, expected',[
    (101, ValueError),
    ('3.13', TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(bank_account, data,expected):
    with pytest.raises(expected):
        bank_account.withdraw(data)