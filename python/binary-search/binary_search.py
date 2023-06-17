"""Exercism's Binary Search Challenge."""


def find(search_list: list[int], value: int) -> int:
    """Find an item in a list via binary search method."""
    low, high = 0, len(search_list)-1
    while high >= low:
        mid = (high + low) // 2
        cur = search_list[mid]
        if cur == value:
            return mid
        elif cur > value:
            high = mid - 1
        else:
            low = mid + 1
    raise ValueError("value not in array")
