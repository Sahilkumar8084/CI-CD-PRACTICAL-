from src.math_operations import add,sub

def test_add():
    assert add(3,5) == 8
    assert add(8,5) ==13
    assert add(45,5) ==50
    assert add(43,5) ==48
    assert add(3,45) ==48
    assert add(34,5) ==39
    
def test_sub():
    assert sub(5,3) ==2
    assert sub(8684,21) == 8663