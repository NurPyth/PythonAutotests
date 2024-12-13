import selenium
import pytest

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')

def test_demo2(before_after):
    assert 2 == 2

def test_demo():
    assert 2 == 2