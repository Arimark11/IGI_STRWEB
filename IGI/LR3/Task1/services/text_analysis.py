"""
Purpose: Text analysis functions,
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

# ---------- Existing functions (Task 2 & 3) ----------

def count_words_starting_with_lowercase(text):
    """Counts words starting with lowercase."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    words = text.split()
    count = 0
    for word in words:
        if word and word[0].islower():
            count += 1
    return count

def count_non_whitespace_chars(text):
    """Counts non‑whitespace characters."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    count = 0
    for ch in text:
        if not ch.isspace():
            count += 1
    return count

# ---------- Functions for Task 4 ----------
def splitting_into_words(text):
    """Split text into words using separators: space, comma, dot."""
    sep = set(',. ')
    words = []
    current_word = []
    for char in text:
        if char in sep:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        words.append(''.join(current_word))
    return words

def semicolon_words(text):
    """Split text into words using space and dot as separators (preserves commas)."""
    sep = set(' .')
    words = []
    current_word = []
    for char in text:
        if char in sep:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        words.append(''.join(current_word))
    return words

def found_word_with_comma(words_list):
    """Return a comma‑separated string of words that end with a comma."""
    result = []
    for w in words_list:
        if w and w[-1] == ',':
            result.append(w)
    return ", ".join(result)

def found_min_words(words_list):
    """Count how many words have the minimal length."""
    if not words_list:
        return 0
    min_len = min(len(w) for w in words_list)
    return sum(1 for w in words_list if len(w) == min_len)

def found_words_with_y(words_list):
    """Return a comma‑separated string of words that end with 'y'."""
    result = []
    for w in words_list:
        if w and w[-1] == 'y':
            result.append(w)
    return ", ".join(result)

def found_max_words_with_y(words_string):
    """Find the longest word from a comma‑separated string of words ending with 'y'."""
    if not words_string:
        return ""
    words = words_string.split(", ")
    if not words:
        return ""
    return max(words, key=len)

