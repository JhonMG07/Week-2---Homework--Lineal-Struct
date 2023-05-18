import pytest
from src.word_count import read_file_and_word_count


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "./01_dicts/test/file1.txt",
            {"a": 1, "is": 1, "file": 1, "sample": 1, "text": 1, "this": 2},
        ),
        ("./01_dicts/test/file2.md", None),
    ],
)
def test__read_file_and_word_count_function__return_dict_or_none__depending_on_the_input_file(
    test_input, expected
):
    response = read_file_and_word_count(test_input)
    assert response == expected
