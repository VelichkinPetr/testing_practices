import os

import pytest
from mod_4_task_4.Logger.Logger import Logger


@pytest.fixture(scope= 'function')
def logger():
    path_to_test_file = 'test_log.txt'
    logger = Logger(path_to_test_file)

    yield logger

    os.remove(path_to_test_file)

@pytest.mark.log
@pytest.mark.parametrize('data, expected',[
    ('11','11'),
    ('qwerty','qwerty'),
    ('Кара','Кара'),
    ('True', 'True'),
    ('Hello world!', 'Hello world!')
])

def test_positive(logger,data,expected):
    logger.log(data)
    assert logger.get_logs()[0].replace('\n', '') == expected

@pytest.mark.log
@pytest.mark.parametrize('data, expected',[
    ('',''),
    ('\n',''),
    (' ',' '),
    (' \n',' ')
])

def test_bound(logger, data,expected):
    logger.log(data)
    assert logger.get_logs()[0].replace('\n', '') == expected

@pytest.mark.log
@pytest.mark.parametrize('data, expected',[
    (-1, TypeError),
    (3.13, TypeError),
    (None, TypeError),
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(logger, data,expected):
    with pytest.raises(expected):
        logger.log(data)
        logger.get_logs()[0].replace('\n', '')
