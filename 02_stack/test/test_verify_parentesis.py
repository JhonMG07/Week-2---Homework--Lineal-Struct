import pytest
from src.verify_partentesis import verify_parentheses

_test_data = [
    {"parentheses": "{{[]}}", "expected": True},
    {"parentheses": "([{}}}])", "expected": False},
    {"parentheses": "{[A}", "expected": None},
    {"parentheses": "1[]1", "expected": None},
]


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        (_test_data[0]["parentheses"], _test_data[0]["expected"]),
        (_test_data[1]["parentheses"], _test_data[1]["expected"]),
        (_test_data[2]["parentheses"], _test_data[2]["expected"]),
        (_test_data[3]["parentheses"], _test_data[3]["expected"]),
    ],
)
def test__verify_parentheses_function__return_true_false_when_input_string_of_parenthesis(
    input_data, expected_output
):
    response = verify_parentheses(input_data)

    assert response == expected_output
