#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by padding with zeros
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Create a new tuple with the sum of the first two elements of each tuple
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)  # Output: (89, 100)

    print(add_tuple(tuple_a, (1, )))  # Output: (2, 89)
    print(add_tuple(tuple_a, ()))    # Output: (1, 89)
