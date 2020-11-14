from typing import List


def binary_search_iter(lst: List[int], key: int) -> int:
    """
    Iterative Binary Search Function
    It returns location of x in given array test_lst if present,
    else returns -1
    'Array' from flowchart == 'lst'
    """
    start = 0
    end = len(lst) - 1

    while start <= end:

        mid = int(start + (end - start) / 2)

        # Check if x is present at mid
        if lst[mid] == key:
            return mid

        # If key is greater, ignore left half
        elif lst[mid] < key:
            start = mid + 1

        # If key is smaller, ignore right half
        else:
            end = mid - 1

    # If we reach here, then the element was not present
    return -1


# Test array
test_lst = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search_iter(test_lst, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")