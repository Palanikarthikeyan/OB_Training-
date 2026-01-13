import pytest

@pytest.fixture
def baseFunc():
    return 10

@pytest.mark.parametrize('value',[10,2,3])
def test_add_with_fixture(baseFunc,value):
    assert baseFunc + value >10