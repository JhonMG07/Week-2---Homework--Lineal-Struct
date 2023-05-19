import pytest
from src.unit_conversion import read_number_and_convert_to_destiantion_unit

_test_data = [
    {
        "input_number": 1000,
        "origin_unit": "m",
        "destination_unit": "km",
        "expected": 1.0,
    },
    {
        "input_number": 1.0,
        "origin_unit": "km",
        "destination_unit": "m",
        "expected": 1000.0,
    },
    {
        "input_number": 1.0,
        "origin_unit": "kl",
        "destination_unit": "m",
        "expected": None,
    },
    {
        "input_number": 4,
        "origin_unit": "km",
        "destination_unit": "cn",
        "expected": None,
    },

]


@pytest.mark.parametrize(
    "input_number,origin_unit,destination_unit,expected",
    [
        (_test_data[0]["input_number"],_test_data[0]["origin_unit"],_test_data[0]["destination_unit"],_test_data[0]["expected"]),
        (_test_data[1]["input_number"],_test_data[1]["origin_unit"],_test_data[1]["destination_unit"],_test_data[1]["expected"]),
        (_test_data[2]["input_number"],_test_data[2]["origin_unit"],_test_data[2]["destination_unit"],_test_data[2]["expected"]),
        (_test_data[3]["input_number"],_test_data[3]["origin_unit"],_test_data[3]["destination_unit"],_test_data[3]["expected"]),

    ],
)
def test__read_number_and_convert_to_destiantion_unit_function__return_the_numer_or_none_depending_on_the_input_cases(
    input_number, origin_unit, destination_unit, expected
):
    response = read_number_and_convert_to_destiantion_unit(
        input_number, origin_unit, destination_unit
    )

    assert response == expected
