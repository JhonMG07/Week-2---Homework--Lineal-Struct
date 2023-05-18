import pytest
from src.unit_conversion import read_number_and_convert_to_destiantion_unit


@pytest.mark.parametrize(
    "input_number,origin_unit,destination_unit,expected",
    [
        (1000.0, "m", "km", 1.0),
        (1.0, "km", "m", 1000.0),
        (1.0, "kl", "m", None),
        (4, "km", "cn", None),
    ],
)
def test__read_number_and_convert_to_destiantion_unit_function__return_the_numer_or_none_depending_on_the_input_cases(
    input_number, origin_unit, destination_unit, expected
):
    response = read_number_and_convert_to_destiantion_unit(
        input_number, origin_unit, destination_unit
    )

    assert response == expected
