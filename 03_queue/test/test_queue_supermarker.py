import pytest
from src.queue_supermarker import add_clients_to_the_queue

_test_data = [
    {"list_client": [1, 2, 3, 4, 5, 6], "empty_list": []},
    {"list_client": ["a", "b", "c"], "empty_list": []},
]


@pytest.mark.parametrize(
    "client_list, empty_list",
    [
        (_test_data[0]["list_client"], _test_data[0]["empty_list"]),
        (_test_data[1]["list_client"], _test_data[1]["empty_list"]),
    ],
)
def test_add_client_to_the_queue__return_client_list__when_pass_client(
    client_list, empty_list
):
    response = add_clients_to_the_queue(client_list)

    assert response == empty_list
