import random
import time


def add_clients_to_the_queue(list_client: list) -> list:
    
    while list_client:
        #time.sleep(random.random() * 2)
        list_client.pop(0)

    return list_client
