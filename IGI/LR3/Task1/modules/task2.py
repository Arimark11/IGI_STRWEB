"""
Purpose: Task 2 – Count non‑negative integers until a number < -100 is entered,
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.validation import get_int
from modules.menu_logic import menu_for_tasks

def count_positive_numbers():
    """
    Reads integers from the user. Counts non‑negative numbers (>= 0).
    Stops when a number less than -100 is entered.
    """
    count = 0
    while True:
        print("Input num > -100")
        num = get_int("Enter number: ")
        if num < -100:
            print("Exit num < -100")
            break
        elif num >= 0:
            count += 1
    print("Result:", count)

@menu_for_tasks
def task2():
    """Main business function for Task 2."""
    count_positive_numbers()