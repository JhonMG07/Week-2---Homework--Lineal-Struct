import pytest
from src.reverse_string import reverse_string

_test_data = [
    {"input": "hello", "output": "olleh"},
    {"input": "hello world", "output": "dlrow olleh"},
    {"input": "I love IOET", "output": "TEOI evol I"},
    {"input": "Jhon", "output": "nohJ"},
]
@pytest.mark.parametrize(
    "origin_string,reverse_string_expected",
    [
        (_test_data[0]["input"], _test_data[0]["output"]),
        (_test_data[1]["input"], _test_data[1]["output"]),
        (_test_data[2]["input"], _test_data[2]["output"]),
        (_test_data[3]["input"], _test_data[3]["output"]),
    ],
)
def test__reverse_string_function__return_reversed_string_when_input_string(
    origin_string, reverse_string_expected
):
    response = reverse_string(origin_string)
    assert response == reverse_string_expected
