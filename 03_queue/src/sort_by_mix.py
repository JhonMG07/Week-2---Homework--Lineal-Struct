# Merge Sort (also known as Merge Sort) is an efficient sorting algorithm that divides an unordered list into two equal (or approximately equal) sublists.
# sorting algorithm that splits an unordered list into two sublists of equal (or approximately equal) size,
# recursively sorts them and then mixes them to obtain a complete sorted list.

# The main idea behind the algorithm is to repeatedly split the list into halves until there are # sublists of size 1 or # equal size.
# sublists of size 1 or 0, which are already considered sorted.

from queue import Queue

def merge_sort_queue(arr: list):
    # caso que solo sea un elemento
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

    # Return the resulting queue as a list
    return list(result.queue)


numeros: list = [9, 3, 1, 7, 2, 8, 5, 4, 6]
print("Lista original:", numeros)

ordenados = merge_sort_queue(numeros)
print("Lista ordenada:", ordenados)
