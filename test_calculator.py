from calculator import add, calculate_average

def test_add():
    assert add(2, 3) == 5

def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20

def test_calculate_average_empty():
    assert calculate_average([]) == 0
