import string


def alphabet_check(s: str) -> bool:
    """
    Check a string `s` has all letters of the alphabet

    :param s: a string input, potentially a mixture of upper and lower case, numbers, special characters etc.
    :return: True if the string contains at least one of each letter of the alphabet. False if not.
    """
    alphabet = set(string.ascii_lowercase)
    s = s.lower()
    return alphabet.issubset(s)
