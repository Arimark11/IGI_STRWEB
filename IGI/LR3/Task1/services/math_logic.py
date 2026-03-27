"""
Purpose: Mathematical calculations (Taylor series for e^x),
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

import math

def calculate_decorator(func):
    """Simple decorator that prints a message before and after calculation."""
    def wrapper(*args, **kwargs):
        print(f"\n--- Starting calculation for x = {args[0]} ---")
        result = func(*args, **kwargs)
        print("--- Calculation finished ---")
        return result
    return wrapper

@calculate_decorator
def calculate_exp_taylor(x, eps):
    """
    Calculate e^x using Taylor series expansion.
    Returns [x, n, approximation, math.exp(x), eps]
    """
    max_iter = 500
    term = 1.0
    total = term
    n = 1

    while n <= max_iter:
        term *= (x / n)
        total += term
        if abs(term) < eps:
            return [x, n, total, math.exp(x), eps]
        n += 1

    return [x, n-1, total, math.exp(x), eps]