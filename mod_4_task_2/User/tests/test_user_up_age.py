from mod_4_task_2.User.user import User
import pytest

@pytest.mark.parametrize('name, age, delta, expected',[
    ('Ivan',12,2,14),
    ('Dmitry',55,5,60),
    ('Petr',25,53,78)
])

def test_positive(name, age, delta, expected):
    assert User(name,age).up_age(delta) == expected


@pytest.mark.parametrize('name, age, delta, expected',[
    ('L',1,-1,2),
    ('1',1,0,1),
    ('Ivan',1,99,100)
])

def test_bound(name, age, delta, expected):
    assert User(name,age).up_age(delta) == expected


@pytest.mark.parametrize('name, age, delta, expected',[
    ('Ivan',1,'2',TypeError),
    ('Ivan',1,100,ValueError),
    ('Ivan',1,[1],TypeError),
    ('Ivan',1,None,TypeError)
])

def test_negative(name, age, delta, expected):
    with pytest.raises(expected):
        User(name,age).up_age(delta)