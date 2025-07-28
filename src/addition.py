
#This is a python addition function
#This is for testing github actions


def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
