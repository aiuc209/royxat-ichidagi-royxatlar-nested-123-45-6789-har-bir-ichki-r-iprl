import pytest

def sum_of_nested_lists(nested_list):
    return [sum(inner_list) for inner_list in nested_list]

def test_sum_of_nested_lists():
    nested_list = [[1,2,3], [4,5], [6,7,8,9]]
    expected_result = [6, 9, 30]
    assert sum_of_nested_lists(nested_list) == expected_result

def test_sum_of_nested_lists_empty():
    nested_list = []
    expected_result = []
    assert sum_of_nested_lists(nested_list) == expected_result

def test_sum_of_nested_lists_single_element():
    nested_list = [[1]]
    expected_result = [1]
    assert sum_of_nested_lists(nested_list) == expected_result

def test_sum_of_nested_lists_negative_numbers():
    nested_list = [[-1, -2, -3], [-4, -5], [-6, -7, -8, -9]]
    expected_result = [-6, -9, -30]
    assert sum_of_nested_lists(nested_list) == expected_result
