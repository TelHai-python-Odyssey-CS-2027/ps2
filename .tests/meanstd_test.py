from math_utils import find_mean_std
import math

def test_find_mean_std():
    # Test case 1
    numbers = (1, 2, 3)
    expected_mean = 2.0
    expected_std = math.sqrt(((1 - 2) ** 2 + (2 - 2) ** 2 + (3 - 2) ** 2) / 3)
    mean, std = find_mean_std(*numbers)
    assert mean == expected_mean #, f"Expected mean {expected_mean}, but got {mean}"
    assert math.isclose(std, expected_std) #, f"Expected std {expected_std}, but got {std}"
    
    # Test case 2
    numbers = (10, 10, 10)
    expected_mean = 10.0
    expected_std = 0.0
    mean, std = find_mean_std(*numbers)
    assert mean == expected_mean #, f"Expected mean {expected_mean}, but got {mean}"
    assert std == expected_std #, f"Expected std {expected_std}, but got {std}"
    
    # Test case 3
    numbers = (4, 8, 12)
    expected_mean = 8.0
    expected_std = math.sqrt(((4 - 8) ** 2 + (8 - 8) ** 2 + (12 - 8) ** 2) / 3)
    mean, std = find_mean_std(*numbers)
    assert mean == expected_mean #, f"Expected mean {expected_mean}, but got {mean}"
    assert math.isclose(std, expected_std) #, f"Expected std {expected_std}, but got {std}"
    
