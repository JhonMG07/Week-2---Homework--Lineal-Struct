import pytest
from src.grade_book import get_average_for_each_student, get_average_of_the_whole_class

_test_data = [
    {
        "grades": {"Jhon": [10, 9.5, 8], "Maria": [9, 8, 7], "Pedro": [8, 7, 6]},
        "expected_grade": {"Jhon": 9.17, "Maria": 8.00, "Pedro": 7.00}
    },
    {
        "grades": {"Alex": [10, "A", 8], "Maria": [9, 8, 7], "Pedro": [8, 7, 6]},
        "expected_grade": None
    },
    {
        "grades": {"Juan": [10, 6.8, 8], "Maria": [9, -10, 7], "Pedro": [8, 7, 6]},
        "expected_grade": None
    }
]

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (_test_data[0]["grades"], _test_data[0]["expected_grade"]),
        (_test_data[1]["grades"], _test_data[1]["expected_grade"]),
        (_test_data[2]["grades"], _test_data[2]["expected_grade"]),
    ],
)
def test__get_average_for_each_student_function__return_dict_or_none__depending_the_content_of_the_list(
    test_input, expected
):
    response = get_average_for_each_student(test_input)
    assert response == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"Jhon": 10.0, "Maria": 10.0, "Pedro": 10.0}, 10),
        ({"Alex": 9.5, "Maria": 9.0, "Pedro":8}, 8.83),
    ],
)
def test__get_average_of_the_whole_class_function__return_float__when_send_the_avgs(
    test_input, expected
):
    response = get_average_of_the_whole_class(test_input)
    assert response == expected
