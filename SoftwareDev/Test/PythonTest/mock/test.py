from unittest.mock import Mock
# from pytest_mock import MockerFixture
from db import *
from pytest_mock import MockerFixture
from unittest.mock import patch
from myclass import *

def test_basics():
    mock = Mock()
    mock.a()
    mock.a.assert_called()
    mock.b.assert_not_called()
    mock.b()
    print(f'mock calls: {mock.mock_calls}')

def test_myclass_function():
    with patch.object(MyClass, 'sayhi', return_value="hi i'm a mock object") as a:
        assert myclass_function() == "hi i'm a mock object"

def test_db(mocker: MockerFixture):
    mock = mocker.patch.object(DB, 'insert', return_value="hi i'm a mock db")
    



if __name__ == '__main__':
    # basics()
    test_myclass_function()
    pass