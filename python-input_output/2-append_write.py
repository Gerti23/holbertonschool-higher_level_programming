#!/usr/bin/python3
"""Module that contains the function append_write."""


def append_write(filename="", text=""):
    """Writes a string to a text file (UTF8)

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)  # Use write() instead of append()
