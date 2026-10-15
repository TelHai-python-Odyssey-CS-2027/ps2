from math_utils import find_max_number

def test_max():
    print("start the test")
    assert find_max_number(1,2,3) == 3
    assert find_max_number(3,1,2) == 3
    assert find_max_number(2,3,1) == 3
    assert find_max_number(-3,-2,-1) == -1
    assert find_max_number(2,3,3) == 3
    assert find_max_number(3,3,2) == 3
    assert find_max_number(3,3,3) == 3
    assert find_max_number(3.3,2.2,1.1) == 3.3
