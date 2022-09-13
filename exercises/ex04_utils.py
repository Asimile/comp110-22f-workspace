"""Utility functions of lists."""

__author__: "730575620"

def all(int_list: list[int], single_int: int) -> bool:
    i: int = 0
    while i < len(int_list) - 1:
        if int_list[i] != single_int:
            return False
        i += 1
    return True


def max(max_list: list[int]) -> int:
    maximum: int = 0
    i: int = 1
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    elif len(max_list) == 1:
        maximum = max_list[0]
        return maximum
    else:
        maximum = max_list[0]
        while i <= len(max_list) - 1:
            if max_list[i] > max_list[i -1]:
                maximum = max_list[i]
            i += 1
        return maximum


def is_equal(first_list: list(int), second_list: list(int)) -> bool:
    if len(first_list) != len(second_list):
        return False
    i: int = 0
    while i < len(first_list):
        if first_list[i] != second_list[i]:
            return False
    return True