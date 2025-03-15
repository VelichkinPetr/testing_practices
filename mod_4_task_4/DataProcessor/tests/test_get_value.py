import pytest,json,os
from mod_4_task_4.DataProcessor.DataProcessor import DataProcessor


@pytest.fixture(scope= "session")
def data_json():
    data = {
        "name": "John",
        "age": 30,
        "isStudent": False,
        "courses": ["Math", "Science"],
        "address": {
            "city": "New York",
            "zip": "10001"
        }
    }
    with open("data_test.json", "w") as write_file:
        json.dump(data, write_file)
    data_processor = DataProcessor("data_test.json")
    print(data_processor)
    yield data_processor
    print(data_processor)
    os.remove("data_test.json")

@pytest.mark.DP
@pytest.mark.parametrize("key, expected",[
    ("name", "John"),
    ("courses", ["Math", "Science"]),
    ("address", {"city": "New York","zip": "10001"}),
    ("age", 30),
    ("isStudent", False),
])

def test_positive(data_json, key, expected):
    assert data_json.get_value(key) == expected

@pytest.mark.DP
@pytest.mark.parametrize('key, expected',[
    ('',None),
    ('names', None),
    (-1, None),
    (3, None),
    (3.14, None),
    (None, None),
    (True, None)
])

def test_bound(data_json, key, expected):
    assert data_json.get_value(key) == expected

@pytest.mark.DP
@pytest.mark.parametrize('key, expected',[
    ([121], TypeError),
    ([], TypeError)
])

def test_negative(data_json, key, expected):
    with pytest.raises(expected):
        data_json.get_value(key)
