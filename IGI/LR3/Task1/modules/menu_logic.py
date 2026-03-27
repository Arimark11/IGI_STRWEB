"""
Purpose: Menu handling decorator,
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

def menu_for_tasks(func):
    """Decorator that adds a menu header and footer around the task."""
    def wrapper(*args, **kwargs):
        print("\n" + "="*70)
        print(f"Running {func.__name__}".center(70))
        print("="*70)
        result = func(*args, **kwargs)
        print("="*70)
        print("Task completed. Returning to main menu...")
        return result
    return wrapper