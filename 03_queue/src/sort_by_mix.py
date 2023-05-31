
from queue import Queue

def merge_sort_queue(arr: list):
    if len(arr) <= 1:
        return arr
    
    # The colon (:) before mid indicates that a portion of the arr list should be taken,
    # from start to index mid-1 for left, and from index mid to end
    # for right. 

    mid: int = len(arr) // 2
    left_list = arr[:mid]
    right_list= arr[mid:]
    
    
    # Recursively sort each sub-list

    left = merge_sort_queue(left_list)
    right = merge_sort_queue(right_list)

    # Mixing the two resulting tails into one neat tail

    result: Queue = Queue()
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.put(left.pop(0))
        else:
            result.put(right.pop(0))

    # Add any remaining elements to the resulting queue

    while len(left) > 0:
        result.put(left.pop(0))
    while len(right) > 0:
        result.put(right.pop(0))

    return list(result.queue)
