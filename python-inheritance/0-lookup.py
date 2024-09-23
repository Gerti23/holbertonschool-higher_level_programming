#!/usr/bin/python3
def lookup(obj):
    """
    Returns the dictionary representation of an object's attributes.

    Args:
        obj: The object whose attributes are to be returned.

    Returns:
        dict: A dictionary containing the object's attributes and their values.
    """
    return obj.__dict__
