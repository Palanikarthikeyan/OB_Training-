import pytest
@pytest.fixture
def f1():
    n = 50
    return n

def test_f1(f1):
    assert f1 == 50

def test_f2(f1):
    assert f1 % 3 == 0


@pytest.fixture
def sample_data():
    return [10,20,30,40]

def test_list_length(sample_data):
    assert len(sample_data) == 5