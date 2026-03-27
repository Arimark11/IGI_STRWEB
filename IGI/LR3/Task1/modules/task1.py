"""
Purpose: Task 1 Exponential function series expansion,
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.math_logic import calculate_exp_taylor
from services.validation import get_float
from modules.menu_logic import menu_for_tasks

def print_table(all_data):
    """Print the results in a formatted table."""
    print("\n" + "="*80)
    print(f"| {'x':^12} | {'n':^6} | {'F(x)':^16} | {'Math F(x)':^16} | {'eps':^10} |")
    print("-"*80)
    for row in all_data:
        print(f"| {row[0]:12.4f} | {row[1]:6d} | {row[2]:16.8f} | {row[3]:16.8f} | {row[4]:10.1e} |")
    print("="*80)

@menu_for_tasks
def task1():
    """Main business function for Task 1."""
    x = get_float("Please enter x = ")
    eps = get_float("Please enter eps = ", min_val=0, max_val=1)
    try:
        result = calculate_exp_taylor(x, eps)
        print_table([result])
    except Exception as e:
        print(f"An error occurred during calculation: {e}")