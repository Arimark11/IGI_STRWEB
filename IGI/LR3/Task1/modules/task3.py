"""
Purpose: Task 3 Count words starting with a lowercase letter,
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.text_analysis import count_words_starting_with_lowercase
from modules.menu_logic import menu_for_tasks

@menu_for_tasks
def task3():
    """Main business function for Task 3."""
    text = input()
    try:
        count = count_words_starting_with_lowercase(text)
        print(f"\nResult: {count} word(s) start with a lowercase letter.")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")