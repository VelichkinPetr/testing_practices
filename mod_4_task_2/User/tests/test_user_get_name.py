from mod_4_task_2.User.user import User
import pytest

@pytest.mark.parametrize('name, age, expected',[
    ('Ivan',12,'Ivan'),
    ('Dmitry',55,'Dmitry'),
    ('Petr',25,'Petr')
])

def test_positive(name, age, expected):
    assert User(name,age).get_name() == expected


@pytest.mark.parametrize('name, age, expected',[
    ('L',1,'L'),
    ('1',2,'1'),
    ('Ivan',1,'Ivan'),
    ('Ivan',100,'Ivan')
])

def test_bound(name, age, expected):
    assert User(name,age).get_name() == expected


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
        User(name,age).get_name()