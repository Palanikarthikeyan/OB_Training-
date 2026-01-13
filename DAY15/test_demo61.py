import pytest
@pytest.mark.parametrize("a,b,expected",
 [ (10,20,30),(100,200,300),(120,30,50)])

def test_calc(a,b,expected):
	assert a+b == expected 