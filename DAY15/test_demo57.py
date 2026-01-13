
import pytest
@pytest.mark.calc
def test_calc_code():
	n = 150
	assert n >100

@pytest.mark.calc
def test_calc_step():
	n = 200
	assert n <= 300

@pytest.mark.sample
def test_equality():
	assert 10 == 11
