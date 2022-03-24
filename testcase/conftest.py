import pytest


@pytest.fixture(scope='function')
def my_fixture():
    print("前置")
    yield
    print('后置')