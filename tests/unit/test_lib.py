import lib
import random


def test_alphabet_check_is_not_case_sensitive():
    """
    Sanity check: can we handle uppercase, lowercase, and mixed case strings
    """
    mixed_case = "abcDEFghijKLmnopqrSTuvwxyZ"
    lowercase = mixed_case.lower()
    uppercase = mixed_case.upper()
    assert lib.alphabet_check(mixed_case) is True
    assert lib.alphabet_check(lowercase) is True
    assert lib.alphabet_check(uppercase) is True


def test_alphabet_check_handles_empty_string():
    """
    Sanity check: should return false for empty string
    """
    assert lib.alphabet_check("") is False


def test_alphabet_check_does_not_crash_with_unicode():
    """
    Sanity check: Unicode always seem to break things...
    """
    falsy = "你好世界"
    truthy = "你好世界abcdefghijklmnopqrstuvwxyz"
    assert lib.alphabet_check(falsy) is False
    assert lib.alphabet_check(truthy) is True


def test_alphabet_check_order_and_other_chars_do_not_matter():
    """
    Alphabet characters should be in any order, with spaces and other characters potentially in between
    """
    random.seed("test")  # ensure test can be reproduced, shuffles will always be the same for the same seed

    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    assert lib.alphabet_check(''.join(letters)) is True

    letters_with_spaces = list("a     bcdefghijk    lmnopq    rstuvwxyz")
    random.shuffle(letters_with_spaces)
    assert lib.alphabet_check(''.join(letters_with_spaces)) is True

    letters_with_other_chars = list("abcdefghijklmnopqrstuvwxyz324823412#@#!@#R?ADS::@#$!$E!@ED你好世界        ")
    random.shuffle(letters_with_other_chars)
    assert lib.alphabet_check(''.join(letters_with_other_chars)) is True

    missing_z = list("abcdefghijklmnopqrstuvwxy324823412#@#!@#R?ADS::@#$!$E!@ED你好世界        ")
    random.shuffle(missing_z)
    assert lib.alphabet_check(''.join(missing_z)) is False
