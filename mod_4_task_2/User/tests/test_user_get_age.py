from mod_4_task_2.User.user import User
import pytest

@pytest.mark.parametrize('name, age, expected',[
    ('Ivan',12,12),
    ('Dmitry',55,55),
    ('Petr',25,25)
])

def test_positive(name, age, expected):
    assert User(name,age).get_age() == expected


@pytest.mark.parametrize('name, age, expected',[
    ('L',1,1),
    ('1',2,2),
    ('Ivan',1,1),
    ('Ivan',100,100)
])

def test_bound(name, age, expected):
    assert User(name,age).get_age() == expected


@pytest.mark.parametrize('name, age, expected',[
    ('',1,ValueError),
    ('   ',[55],TypeError),
    ('   ',55,ValueError),
    ('Ivan','0',TypeError),
    ('Ivan',0,ValueError),
    ('Ivan',101,ValueError)
])

def test_negative(name, age,expected):
    with pytest.raises(expected):
        User(name,age).get_age()