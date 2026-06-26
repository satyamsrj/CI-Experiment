# src/cal_test.py
import pytest

# Define the functions here so pytest can test them
def add(x, y): 
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y): 
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

# ------------------ Tests ------------------

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_invalid_inputs():
    with pytest.raises(TypeError):
        add("String", 5)
    with pytest.raises(TypeError):
        subtract(10, "b")
    with pytest.raises(TypeError):
        multiply(None, 3)
    with pytest.raises(TypeError):
        divide("x", 2)
