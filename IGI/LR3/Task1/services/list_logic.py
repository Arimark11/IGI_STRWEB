"""
Purpose: Functions for list operations (generation, input, max absolute value, sum between two positives),
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

import random
from services.validation import get_float

def list_generator(size: int) -> list:
    """Generates a list of random floats in range [-10, 10] with two decimals."""
    return [round(random.uniform(-10, 10), 2) for _ in range(size)]

def input_list(size: int) -> list:
    """Initializes a list with user input (floats)."""
    lst = []
    for i in range(size):
        lst.append(get_float(f"Enter element №{i+1}: "))
    return lst

def max_abs_element(lst: list):
    """Returns the element with the maximum absolute value."""
    if not lst:
        return None
    max_abs = lst[0]
    for val in lst[1:]:
        if abs(val) > abs(max_abs):
            max_abs = val
    return max_abs

def sum_between_first_second_positive(lst: list):
    """
    Returns the sum of elements located between the first and second positive elements.
    Does not include the positive elements themselves.
    If there are fewer than two positive elements, returns None.
    """
    positives = []
    for idx, val in enumerate(lst):
        if val > 0:
            positives.append(idx)
            if len(positives) == 2:
                break
    if len(positives) < 2:
        return None
    first, second = positives[0], positives[1]
    if second - first <= 1:
        return 0
    return sum(lst[first+1:second])