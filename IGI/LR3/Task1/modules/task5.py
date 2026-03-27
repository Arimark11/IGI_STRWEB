"""
Purpose: Task 5 Find max absolute element and sum between first and second positive,
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.validation import get_int
from services.list_logic import list_generator, input_list, max_abs_element, sum_between_first_second_positive
from modules.menu_logic import menu_for_tasks

def input_method():
    """Select a method for entering the list (manual input or generator)."""
    size = get_int("List size: ", min_val=0)
    print("1. Manual Input | 2. Generator")
    while True:
        method = get_int("Choice: ")
        if method == 1:
            return input_list(size)
        elif method == 2:
            return list_generator(size)
        else:
            print("Enter 1 or 2!")

@menu_for_tasks
def task5():
    """Main business function for Task 5."""
    # 1. Create the list
    my_list = input_method()
    print("\nCreated list:", my_list)

    # 2. Find maximum absolute element
    max_abs = max_abs_element(my_list)
    if max_abs is not None:
        print(f"Maximum absolute element: {max_abs}")
    else:
        print("List is empty.")

    # 3. Sum between first and second positive elements
    total = sum_between_first_second_positive(my_list)
    if total is None:
        print("There are fewer than two positive elements → cannot compute sum between.")
    else:
        print(f"Sum of elements between the first and second positive elements: {total:.2f}")