from src.math_operations import add,sub

def test_add():
    assert add(3,5) == 8
    assert add(8,5) ==13
    assert add(45,5) ==50
    assert add(43,5) ==48
    assert add(3,45) ==48
    assert add(34,5) ==38
    
def test_sub(): #pytest ko rn karne ke liye hume aise gunction banane honge jinke naam test_ se hoo yaa koi folder ya files  end ho _test .py se aisa kuchh
    assert sub(5,3) ==2
    assert sub(8684,21) == 8663