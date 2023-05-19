import pytest

from src.posfijas import evaluate_posfixed_expression

_test_data = [
    {"expression": "12+", "result": 3},
    {"expression": "12+3+", "result": 6},
    {"expression": "53+82-/", "result": 1.33},
]


@pytest.mark.parametrize(
    "expression, result",
    [
        (_test_data[0]["expression"], _test_data[0]["result"]),
        (_test_data[1]["expression"], _test_data[1]["result"]),
        (_test_data[2]["expression"], _test_data[2]["result"]),
    ],
)
def test_evaluate_posfixed_expression_function__returns_the_result_of_the_operation(
    expression, result
):
    response = evaluate_posfixed_expression(expression)

    assert response == result
