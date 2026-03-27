"""
Purpose: Task 4 Text analysis (min length, words with comma, longest word ending with 'y'),
Lab 3, Version 1.0,
Author: Ermakov Egor,
Date: 2026-03-26.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.text_analysis import (
    splitting_into_words,
    semicolon_words,
    found_word_with_comma,
    found_min_words,
    found_words_with_y,
    found_max_words_with_y
)
from modules.menu_logic import menu_for_tasks

TEXT = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")

@menu_for_tasks
def task4():
    """Main business function for Task 4."""
    words = splitting_into_words(TEXT)
    count_min = found_min_words(words)
    print("---------------------------------")
    print("a) Count of words with minimal length:", count_min)

    words_with_comma = semicolon_words(TEXT)
    comma_words = found_word_with_comma(words_with_comma)
    cleaned = comma_words.replace(",,", ",")
    print("---------------------------------")
    print("b) Words followed by a comma:", cleaned)

    words_with_y = found_words_with_y(words)
    max_word = found_max_words_with_y(words_with_y)
    print("---------------------------------")
    print("c) Longest word ending with 'y':", max_word)
    print("---------------------------------")