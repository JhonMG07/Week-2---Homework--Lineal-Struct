import pytest
from src.sort_by_mix import merge_sort_queue

def test_merge_sort_queue_function__return_sorted_list_when_input_a_unordered_list():

    sorted_list_expected = [1,2,3,4,5]
    unordered_list=[5,3,4,2,1]

    response = merge_sort_queue(unordered_list)
    
    assert response == sorted_list_expected
