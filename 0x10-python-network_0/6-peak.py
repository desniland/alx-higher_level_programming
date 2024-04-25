#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds the peak in a list of integers using an efficient approach.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int or None: The peak value if found, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Move right to find a higher neighbor
            left = mid + 1
        else:
            # Move left to find a higher neighbor
            right = mid

    return list_of_integers[left]
