from math_utils import find_mean

def test_mean():
  assert find_mean(1,2,3) == 2
  assert find_mean(-1,1,0) == 0
