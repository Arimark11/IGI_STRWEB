"""
Purpose: Input validation and data entry,
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

def get_int(prompt="", min_val=None):
    """
    Safely gets an integer from the user with optional minimum value.
    """
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val <= min_val:
                print(f"Error! Please enter a number > {min_val}")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter an integer.")

def get_float(prompt, max_val=None, min_val=None):
    """Safely gets a float from the user (with optional maximum value)."""
    while True:
        try:
            val = float(input(prompt))
            if max_val is not None and val > max_val:
                print(f"Error! Please enter a real number <= {max_val}")
                continue
            if min_val is not None and val <= min_val:
                print(f"Error! Please enter a real number > {min_val}")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter a real number.") 