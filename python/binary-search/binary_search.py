"""Exercism's Binary Search Challenge."""


def find(search_list: list[int], value: int) -> int:
    """Find an item in a list via binary search method."""
    if not search_list:
        raise ValueError("value not in array")
    a, b = 0, len(search_list)-1
    mid: int = b // 2
    while True:
        cur = search_list[mid]
        if cur == value:
            return mid
        elif b <= a:
            raise ValueError("value not in array")
        elif cur > value:
            b = mid - 1
            mid = (b + a) // 2
        else:
            a = mid + 1
            mid = (b + a) // 2
