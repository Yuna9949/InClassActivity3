def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def test_add_pt():
    assert add(10,5) == 15

def test_sub_pt():
    assert sub(10,5) == 5

def test_mul_pt():
    assert mul(10,5) == 50

def test_div_pt():
    assert div(10,5) == 2